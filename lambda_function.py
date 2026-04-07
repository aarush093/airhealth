import json
import numpy as np
import onnxruntime as rt
import os

model_path = os.path.join(os.path.dirname(__file__), "model.onnx")
sess = rt.InferenceSession(model_path)
input_name = sess.get_inputs()[0].name
label_name = sess.get_outputs()[0].name

def lambda_handler(event, context):
    try:
        body = json.loads(event["body"])

        features = np.array([[
            body["temperature"],
            body["vibration"],
            body["pressure"],
            body["runtime_hours"],
            body["error_code_count"]
        ]], dtype=np.float32)

        prediction = sess.run([label_name], {input_name: features})[0][0]
        
        return {
            "statusCode": 200,
            "body": json.dumps({
                "failure_predicted": bool(prediction),
                "status": "NEEDS MAINTENANCE ⚠️" if prediction == 1 else "ALL GOOD ✅"
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
