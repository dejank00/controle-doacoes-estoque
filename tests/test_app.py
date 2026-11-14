from app import app

def test_pagina_inicial():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert b"Controle de Doacoes e Estoque" in response.data
