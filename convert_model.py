import pickle
import numpy as np
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

initial_type = [("float_input", FloatTensorType([None, 5]))]
onnx_model = convert_sklearn(model, initial_types=initial_type, target_opset=15)

with open("model.onnx", "wb") as f:
    f.write(onnx_model.SerializeToString())

print("Model converted to ONNX successfully!")
