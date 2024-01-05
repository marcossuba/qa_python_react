# myproject/app/routes.py
from . import app
from flask import jsonify

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the QA Site Backend!"})
