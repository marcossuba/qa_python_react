from flask import Flask
from .views.main import main_bp

def create_app():
    app = Flask(__name__)
    
    # Configurações do aplicativo
    app.config.from_pyfile('config.py')

    # Registrar blueprints
    app.register_blueprint(main_bp)

    return app