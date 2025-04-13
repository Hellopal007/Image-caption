# backend/caption.py

from flask import Blueprint, jsonify

caption_bp = Blueprint('caption', __name__)

@caption_bp.route('/generate', methods=['POST'])
def generate_caption():
    return jsonify({"caption": "This is a test caption 🤖"})
