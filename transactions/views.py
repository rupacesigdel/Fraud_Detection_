from django.shortcuts import render, redirect, get_object_or_404
from .models import Transaction
from .forms import TransactionForm
from .fraud_detection import detect_fraud  # Import the fraud detection function
from django.contrib import messages  # Import messages framework
from django.db import transaction
from django.db import transaction as db_transaction
import joblib
from django.conf import settings
import os
import pandas as pd


def home(request):
    return render(request, 'transactions/home.html')  # Adjust the path if needed


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

                    # Prepare the data for the fraud detection model
                    new_transaction_data = {
                        'feature1': transaction_instance.feature1,
                        'feature2': transaction_instance.feature2,
                        # Add other features from your Transaction model
                    }

                    # Convert the data to a DataFrame (assuming your model was trained with pandas)
                    new_transaction_df = pd.DataFrame([new_transaction_data])

                    # Predict fraud
                    prediction = fraud_detection_model.predict(new_transaction_df)

                    # Update the transaction instance based on the prediction
                    transaction_instance.is_fraudulent = prediction[0] == 1
                    transaction_instance.save()

                    # Notify the user based on the fraud status
                    if transaction_instance.is_fraudulent:
                        messages.warning(request, 'This transaction has been flagged as potentially fraudulent.')
                    else:
                        messages.success(request, 'Transaction created successfully.')

                    return redirect('transaction_detail', pk=transaction_instance.id)
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
