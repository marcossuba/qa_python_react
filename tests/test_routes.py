from app import create_app

def test_home_page():
    flask_app = create_app()

    # Cria um cliente de teste usando o Flask application configurado
    with flask_app.test_client() as test_client:
        response = test_client.get('/')  # Faz uma requisição GET para a rota '/'
        assert response.status_code == 200  # Verifica se a resposta é 200 OK
        assert b"Hello, World!" in response.data  # Verifica se o corpo da resposta é o esperado

def test_about_page():
    flask_app = create_app()

    with flask_app.test_client() as test_client:
        response = test_client.get('/about')  # Substitua '/about' pela rota que você deseja testar
        assert response.status_code == 200
        assert b"Algum conteúdo esperado" in response.data

def test_404_page():
    flask_app = create_app()

    with flask_app.test_client() as test_client:
        response = test_client.get('/some/nonexistent/route')
        assert response.status_code == 404  # Verifica se a resposta é 404 Not Found
