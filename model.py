import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib


# Load dataset
data = pd.read_csv('inventory.csv')


# Encode storage type
le = LabelEncoder()
data['storage_type'] = le.fit_transform(data['storage_type'])


# Calculate days to expiry
data['days_to_expiry'] = (
pd.to_datetime(data['expiry_date']) - pd.to_datetime(data['today_date'])
).dt.days


X = data[['days_to_expiry', 'daily_sales', 'current_stock', 'storage_type']]
y = data['expiry_risk']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
joblib.dump(model, 'expiry_model.pkl')
print("Model trained successfully")