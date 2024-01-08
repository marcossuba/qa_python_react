def test_404_page():
    flask_app = create_app()

    with flask_app.test_client() as test_client:
        response = test_client.get('/some/nonexistent/route')
        assert response.status_code == 404  # Verifica se a resposta é 404 Not Found
