# backend/auth.py

from flask import Blueprint, jsonify

# Create a Blueprint for auth routes
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login')
def login():
    return jsonify({"message": "Login route under construction 🛠️"})

@auth_bp.route('/logout')
def logout():
    return jsonify({"message": "Logout route under construction 🔒"})
