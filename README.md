# Daikin AC Predictive Maintenance API

A Machine Learning API that predicts AC unit failures based on sensor data.
Deployed on AWS Lambda + API Gateway.

## Tech Stack
- Python
- scikit-learn (Random Forest Classifier)
- ONNX (model format)
- AWS Lambda
- AWS API Gateway
- AWS S3

## How It Works
The model analyzes 5 sensor readings and predicts if an AC unit will fail:
- Temperature
- Vibration
- Pressure
- Runtime Hours
- Error Code Count

## Live API
POST https://1usi5a4d5l.execute-api.ap-south-1.amazonaws.com/default/daikin-predictor

## Test It
import requests

url = "https://1usi5a4d5l.execute-api.ap-south-1.amazonaws.com/default/daikin-predictor"

sick_ac = {
    "temperature": 75,
    "vibration": 9,
    "pressure": 90,
    "runtime_hours": 4500,
    "error_code_count": 15
}

healthy_ac = {
    "temperature": 30,
    "vibration": 2,
    "pressure": 40,
    "runtime_hours": 500,
    "error_code_count": 1
}

print("Sick AC:", requests.post(url, json=sick_ac).json())
print("Healthy AC:", requests.post(url, json=healthy_ac).json())

## Model Performance
- Accuracy: 99.50%
- Precision: 99%
- Recall: 100%
