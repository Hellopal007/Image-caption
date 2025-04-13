# backend/app.py
from flask import Flask
from dotenv import load_dotenv
import os

# Load env vars
load_dotenv(dotenv_path="./backend/.env")

def create_app():
    app = Flask(__name__)

    # Import blueprints
    from auth import auth_bp
    from caption import caption_bp

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(caption_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
