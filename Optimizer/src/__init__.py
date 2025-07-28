# src/__init__.py
from flask import Flask
from dotenv import load_dotenv

def create_app():
    # Load environment variables from .env file
    load_dotenv()

    # Create the Flask app instance
    app = Flask(__name__)

    # Import and register the blueprint from the controller
    from .controllers.ambulance_controller import ambulance_bp
    app.register_blueprint(ambulance_bp)

    print("🚑 Flask App created and routes registered.")
    return app