# backend/app.py

from flask import Flask
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv(dotenv_path="./backend/.env")

def create_app():
    app = Flask(__name__)

    # Example config from env (optional)
    app.config['SECRET_KEY'] = os.getenv("AUTH0_CLIENT_SECRET")

    # Register your blueprints
    from auth import auth_bp
    from caption import caption_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(caption_bp, url_prefix='/caption')

    @app.route('/')
    def home():
        return {"message": "Hackfest backend running 🚀"}

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
