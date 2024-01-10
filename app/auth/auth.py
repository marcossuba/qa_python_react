from flask import Blueprint, request, jsonify
from flask_login import login_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired
from werkzeug.security import check_password_hash
from .models.user import User
from app import db, login_manager
import jwt
import datetime

# Blueprint para autenticação
auth_bp = Blueprint('auth_bp', __name__)

# Classe do formulário para login
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

@auth_bp.route('/login', methods=['POST'])
def login():
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
    return User.query.get(int(user_id))
