from flask import Blueprint, jsonify
from db.queries import fetch_all_phones

phones_bp = Blueprint("phones", __name__)

@phones_bp.route("/api/phones", methods=["GET"])
def get_phones():
    data = fetch_all_phones()
    return jsonify(data)
