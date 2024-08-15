from django.shortcuts import render, redirect, get_object_or_404
from .models import Transaction
from .forms import TransactionForm
from .fraud_detection import detect_fraud  # Import the fraud detection function

def home(request):
    return render(request, 'home.html')

def create_transaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.is_fraudulent = detect_fraud(transaction)  # Call fraud detection
            transaction.save()
            return redirect('transaction_detail', transaction.id)
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
