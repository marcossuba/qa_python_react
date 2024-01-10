"""
Este módulo realiza a autenticação de usuários.
"""

import datetime
from flask import Blueprint, request, jsonify
from flask_login import login_user, LoginManager
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
from werkzeug.security import check_password_hash
from .models import User
from .. import db
import jwt

# Blueprint para autenticação
auth_bp = Blueprint('auth_bp', __name__)

# Classe do formulário para login
class LoginForm(FlaskForm):
    """
    Formulário Flask-WTF para login de usuário.
    """
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Processa a tentativa de login do usuário, verificando as credenciais e
    emitindo um token JWT se bem-sucedido.
    """
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            
            # Gera um token JWT para a sessão do usuário
            token = jwt.encode({
                'user_id': user.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            }, app.config['SECRET_KEY'], algorithm='HS256')

            return jsonify({'token': token}), 200

        return jsonify({'message': 'Invalid username or password'}), 401
    else:
        return jsonify({'message': 'Invalid form inputs'}), 400

@login_manager.user_loader
def load_user(user_id):
    """
    Callback do Flask-Login para carregar um objeto User a partir do ID do usuário,
    usado para recarregar o objeto de usuário a partir do ID armazenado na sessão.
    """
    return User.query.get(int(user_id))
