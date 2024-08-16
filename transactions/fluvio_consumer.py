import fluvio, os
import json
import joblib
import pandas as pd
from .models import Transaction
from django.utils import timezone
from django.conf import settings

model_path = os.path.join(settings.BASE_DIR, 'model.pkl')
fraud_detection_model = joblib.load(model_path)

consumer = fluvio.partition_consumer('transactions', 0)

def process_transaction(transaction_json):
    transaction_data = json.loads(transaction_json)
    df = pd.DataFrame([transaction_data])
    X = df[['feature1', 'feature2', 'amount', 'date', 'location', 'merchant']]
    prediction = fraud_detection_model.predict(X)

    if prediction == -1:
        alert(transaction_data)

def alert(transaction_data):
    print(f"Fraud detected: {transaction_data['transaction_id']}")

    Transaction.objects.create(
        transaction_id=transaction_data['transaction_id'],
        amount=transaction_data['amount'],
        date=transaction_data['date'],
        location=transaction_data['location'],
        merchant=transaction_data['merchant'],
        is_fraud=True,
        created_at=timezone.now()
    )

def start_consumer():
    for message in consumer.stream():
        process_transaction(message.value())

if __name__ == '__main__':
    start_consumer()
