import joblib
import numpy as np

# Load the trained model
model = joblib.load('model.pkl')

def detect_fraud(transaction):
    # Convert transaction data to model input format
    features = np.array([[transaction.amount,1 if transaction.location != "Unknown" else 0, hash(transaction.merchant) % 2]])  # Dummy encoding for merchant

    # Predict fraud
    is_fraud = model.predict(features)[0]
    
    return bool(is_fraud)
