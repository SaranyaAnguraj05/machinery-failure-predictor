# train_model.py
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pickle

# Simulate sensor data
np.random.seed(42)
n = 1000
data = pd.DataFrame({
    'temperature': np.random.normal(75, 10, n),
    'pressure': np.random.normal(30, 5, n),
    'vibration': np.random.normal(0.5, 0.1, n),
    'humidity': np.random.normal(50, 10, n),
    'failure': np.random.choice([0, 1], p=[0.9, 0.1], size=n)
})

# Add failure patterns
data.loc[data['temperature'] > 90, 'failure'] = 1
data.loc[data['vibration'] > 0.7, 'failure'] = 1

# Split data
X = data.drop('failure', axis=1)
y = data['failure']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Print performance
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save model
with open('backend/model.pkl', 'wb') as f:
    pickle.dump(model, f)
