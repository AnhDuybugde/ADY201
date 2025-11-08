from flask import Blueprint, request, jsonify
import numpy as np

predict_bp = Blueprint("predict", __name__)

# ⚠️ Tạm tắt load model
# MODEL_PATH = os.path.join(os.path.dirname(__file__), "../models/price_model.pkl")
# model = joblib.load(MODEL_PATH)

@predict_bp.route("/api/predict", methods=["POST"])
def predict():
    data = request.json
    # Thay vì dùng model, trả về giả định tạm
    fake_price = (data["ram"] * 20 + data["storage"] * 10 + data["battery"] * 0.5)
    return jsonify({"predicted_price": round(fake_price, 2)})
