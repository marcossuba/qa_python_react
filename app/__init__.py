from flask import Flask
from .views.main import main_bp
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://marcossuba:masa2917@localhost/ambiente_desenv'
    
    db.init_app(app)

    # Configurações do aplicativo
    app.config.from_pyfile('../config.py')

    # Registrar blueprints
    app.register_blueprint(main_bp)

    # Registrar rotas
    from .routes import main
    app.register_blueprint(main_bp, name='unique_main')


    return app
