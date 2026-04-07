from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    features = np.array([[
        data["temperature"],
        data["vibration"],
        data["pressure"],
        data["runtime_hours"],
        data["error_code_count"]
    ]])

    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    return jsonify({
        "failure_predicted": bool(prediction),
        "failure_probability": round(float(probability), 2),
        "status": "NEEDS MAINTENANCE ⚠️" if prediction == 1 else "ALL GOOD ✅"
    })

if __name__ == "__main__":
    app.run(debug=True)
