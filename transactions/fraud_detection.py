import os
import joblib
import numpy as np

# Load the pre-trained machine learning model
model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'models', 'fraud_detection_model.pkl')
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    raise FileNotFoundError(f"Model file not found at: {model_path}")

def rule_based_detection(transaction):
    """
    Apply rule-based logic to detect fraud.
    """
    if transaction.amount > 5000:
        return True  # Flag large transactions

    if transaction.location != transaction.user.profile.location:
        return True  # Flag transactions from unusual locations

    if transaction.device != transaction.user.profile.device:
        return True  # Flag transactions from new devices

    # Additional rules can be added here
    
    return False  # If no rules are triggered, consider it non-fraudulent

def ml_based_detection(transaction):
    """
    Use the machine learning model to predict the likelihood of fraud.
    """
    features = np.array([[transaction.amount,1 if transaction.location != "Unknown" else 0,hash(transaction.merchant) % 2]])  # Example features

    # Predict fraud
    is_fraud = model.predict(features)[0]
    
    return bool(is_fraud)

def detect_fraud(transaction):
    """
    Combine rule-based and ML-based detection logic.
    """
    # First, apply rule-based logic
    if rule_based_detection(transaction):
        return True

    # Then apply machine learning model
    if ml_based_detection(transaction):
        return True

    return False
