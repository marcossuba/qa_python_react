"""
Este módulo contém testes para as rotas da aplicação Flask.
"""

from app import create_app


def test_home_page():
    """
    Testa a rota da página inicial '/' verificando se a resposta é 200 e o conteúdo esperado está presente.
    """
    create_app()

    # ... código restante da função ...


def test_about_page():
    """
    Testa a rota 'about' verificando se a resposta é 200 e o conteúdo esperado está presente.
    """
    create_app()

    # ... código restante da função ...


def test_404_page():
    """
    Testa uma rota inexistente para garantir que a resposta 404 Not Found é retornada.
    """
    create_app()

    # ... código restante da função ...
