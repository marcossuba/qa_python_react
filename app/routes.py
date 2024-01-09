# myproject/app/routes.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the QA Site Backend!"})

@app.route('/')
def about():
    return "Aqui vai alguma informação sobre o site ou aplicativo."

if __name__ == '__main__':
    app.run(debug=True)
