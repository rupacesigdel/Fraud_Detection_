import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load your transaction data
data = pd.read_csv('transactions.csv')

# Preprocess the data (handling missing values, encoding categorical features, etc.)
# This step is highly dependent on your dataset

# Split the data into features and labels
X = data.drop('is_fraudulent', axis=1)
y = data['is_fraudulent']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train a RandomForestClassifier (or any other appropriate model)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Use the model to predict fraud on new transactions
new_transaction = pd.DataFrame({
    'feature1': [None],
    'feature2': [None],
    # Add other features
})

prediction = model.predict(new_transaction)
if prediction[0] == 1:
    print("Fraudulent transaction detected!")
else:
    print("Transaction is safe.")


import joblib

# Assuming you have trained your model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, 'model.pkl')
