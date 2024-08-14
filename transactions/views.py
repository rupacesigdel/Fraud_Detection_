from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Transaction
from .forms import TransactionForm
from .fraud_detection import detect_fraud  # Import the combined fraud detection function

@login_required
def create_transaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.is_fraudulent = detect_fraud(transaction)  # Use combined fraud detection
            transaction.save()
            return redirect('transaction_detail', transaction.id)
    else:
        form = TransactionForm()
    return render(request, 'transactions/create_transaction.html', {'form': form})
