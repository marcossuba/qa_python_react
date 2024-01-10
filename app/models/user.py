"""Módulo que define o modelo de usuário para o banco de dados."""

from app import db


class User(db.Model):
    """Modelo de usuário para autenticação. Contém identificador, nome de usuário e hash de senha."""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)

    # Métodos adicionais como para verificar senha, etc.
