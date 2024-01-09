from flask import Blueprint, render_template, redirect, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user
from app.models.user import User, db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    # lógica para verificar usuário e senha
    # ...

@auth.route('/register')
def signup():
    return render_template('register.html')

@auth.route('/register', methods=['POST'])
def signup_post():
    # lógica para criar novo usuário
    # ...

@auth.route('/logout')
def logout():
    logout_user()
    return redirect('/login')
