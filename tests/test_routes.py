from app import create_app

def test_home_page():
    flask_app = create_app()

    with flask_app.test_client() as test_client:
        response = test_client.get('/')  # Faz uma requisição GET para a rota '/'
        assert response.status_code == 200
        data = response.data.decode('utf-8')  # Decodifica os dados de bytes para string
        assert "Welcome to the QA Site Backend!" in data  # Verifica se o corpo da resposta é o esperado

def test_about_page():
    flask_app = create_app()

    with flask_app.test_client() as test_client:
        response = test_client.get('/about')  # Agora testando a rota '/about'
        assert response.status_code == 200
        data = response.data.decode('utf-8')
        assert "Aqui vai alguma informação sobre o site ou aplicativo." in data  # Certifique-se de que isto corresponde ao conteúdo retornado pela rota '/about'

def test_404_page():
    flask_app = create_app()

    with flask_app.test_client() as test_client:
        response = test_client.get('/some/nonexistent/route')
        assert response.status_code == 404  # Verifica se a resposta é 404 Not Found
