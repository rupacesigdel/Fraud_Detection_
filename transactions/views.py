from django.shortcuts import render, redirect, get_object_or_404
from .models import Transaction
from .forms import TransactionForm
from .fraud_detection import detect_fraud
from django.contrib import messages
from django.db import transaction as db_transaction
import joblib
import os
import pandas as pd
from django.conf import settings
from .fluvio_producer import produce_transaction
from django.utils import timezone
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def home(request):
    return render(request, 'transactions/home.html')

model_path = os.path.join(settings.BASE_DIR, 'model.pkl')
fraud_detection_model = joblib.load(model_path)

def create_transaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            try:
                with db_transaction.atomic():
                    transaction_instance = form.save(commit=False)
                    transaction_instance.user = request.user

                    new_transaction_data = {
                        'feature1': transaction_instance.feature1,
                        'feature2': transaction_instance.feature2,
                        'amount': transaction_instance.amount,
                        'date': transaction_instance.date,
                        'location': transaction_instance.location,
                        'merchant': transaction_instance.merchant,
                    }

                    new_transaction_df = pd.DataFrame([new_transaction_data])

                    prediction = fraud_detection_model.predict(new_transaction_df)
                    transaction_instance.is_fraud = prediction[0] == 1
                    transaction_instance.save()

                    if transaction_instance.is_fraud:
                        messages.warning(request, 'This transaction has been flagged as potentially fraudulent.')
                    else:
                        messages.success(request, 'Transaction created successfully.')
                    transaction_data = {
                        'transaction_id': transaction_instance.transaction_id,
                        'amount': transaction_instance.amount,
                        'date': transaction_instance.date.isoformat(),
                        'location': transaction_instance.location,
                        'merchant': transaction_instance.merchant,
                        'is_fraud': transaction_instance.is_fraud,
                    }

                    produce_transaction(transaction_data)

                    return redirect('transaction_detail', pk=transaction_instance.pk)
            except Exception as e:
                messages.error(request, 'An error occurred while creating the transaction.')
                print(f"Error: {e}")
        else:
            messages.error(request, 'There was an error with your submission. Please correct the errors below.')
    else:
        form = TransactionForm()
    
    return render(request, 'transactions/create_transaction.html', {'form': form})

def transaction_detail(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    return render(request, 'transactions/transaction_detail.html', {'transaction': transaction})

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'transactions/transaction_list.html', {'transactions': transactions})

def predict_fraud(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    fraud_result = detect_fraud(transaction)
    return render(request, 'transactions/transaction_detail.html', {'transaction': transaction, 'fraud_result': fraud_result})


def statistics_view(request):
    today = timezone.now().date()
    transactions_today = Transaction.objects.filter(date__date=today)
    data = transactions_today.values('location', 'is_fraud').annotate(count=count('id'))

    areas = {}
    for entry in data:
        location = entry['location']
        is_fraud = entry['is_fraud']
        count = entry['count']
        if location not in areas:
            areas[location] = {'fraud': 0, 'non_fraud': 0}
        if is_fraud:
            areas[location]['fraud'] += count
        else:
            areas[location]['non_fraud'] += count

    charts = []
    for location, counts in areas.items():
        labels = ['Fraud', 'Non-Fraud']
        sizes = [counts['fraud'], counts['non_fraud']]
        
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        plt.title(f'Transactions Distribution for {location} on {today}')

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        plt.close(fig)
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        charts.append({'location': location, 'image': image_base64})

    return render(request, 'transactions/statistics.html', {'charts': charts})