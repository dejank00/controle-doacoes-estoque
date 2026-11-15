import pytest

from services.stock import calculate_balance


def test_calcula_entrada_e_saida():
    assert calculate_balance(10, 5, "entrada") == 15
    assert calculate_balance(10, 5, "saida") == 5


def test_rejeita_saida_maior_que_saldo():
    with pytest.raises(ValueError, match="saída superior"):
        calculate_balance(2, 3, "saida")
