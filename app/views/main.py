from flask import Blueprint

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return "Welcome to the QA Site Backend!"

@main_bp.route('/about')
def about():
    return "Aqui vai alguma informação sobre o site ou aplicativo."