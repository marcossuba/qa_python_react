"""
Este módulo define as rotas para a aplicação Flask.
"""

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    """
    Rota para a página inicial que retorna uma mensagem de boas-vindas.
    """
    return jsonify({"message": "Welcome to the QA Site Backend!"})


@app.route('/about')
def about():
    """
    Rota que fornece informações sobre o site ou aplicativo.
    """
    return "Aqui vai alguma informação sobre o site ou aplicativo.", 200


if __name__ == '__main__':
    app.run(debug=True)

# Nova linha no final do arquivo
