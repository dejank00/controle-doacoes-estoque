from app import app

def test_pagina_inicial():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert "Controle de Doações e Estoque" in response.get_data(as_text=True)


def test_registra_entrada_e_exibe_confirmacao():
    response = app.test_client().post(
        "/movimentacao",
        data={"produto": "Arroz 5 kg", "operacao": "entrada", "quantidade": "2"},
    )
    assert response.status_code == 200
    assert "Movimentação registrada com sucesso" in response.get_data(as_text=True)


def test_rejeita_saida_maior_que_estoque():
    response = app.test_client().post(
        "/movimentacao",
        data={"produto": "Leite em pó", "operacao": "saida", "quantidade": "99"},
    )
    assert "saída superior ao estoque disponível" in response.get_data(as_text=True)
