from flask import Flask
from .views.main import main_bp
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .models.user import db, User

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


db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
