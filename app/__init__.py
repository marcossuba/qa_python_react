"""
Este módulo inicializa a aplicação Flask, configurando a base de dados e registrando blueprints.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .models.user import db, User
from .views.main import main_bp

def create_app():
    """
    Cria e configura uma instância da aplicação Flask.
    """
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        'postgresql://marcossuba:masa2917@localhost/ambiente'
    )
    app.config.from_pyfile('../config.py')
    
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    app.register_blueprint(main_bp, name='unique_main')

    return app

# Certifique-se de que não haja espaços em branco em nenhuma linha em branco.
# Adicione uma nova linha no final do arquivo.
