# backend/app.py
from flask import Flask, request, jsonify
import pickle
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to connect

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = [data['temperature'], data['pressure'], data['vibration'], data['humidity']]
    prediction = model.predict([features])[0]
    result = "Failure Expected 🔴" if prediction == 1 else "Normal ✅"
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)
