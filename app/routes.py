# myproject/app/routes.py
from flask import Flask, jsonify
from flask import Blueprint

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the QA Site Backend!"})

@app.route('/about')
def about():
    return "Aqui vai alguma informação sobre o site ou aplicativo.", 200

if __name__ == '__main__':
    app.run(debug=True)

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "Página Inicial"