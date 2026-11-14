from app import app

def test_pagina_inicial():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert "Controle de Doações e Estoque" in response.get_data(as_text=True)
