VALID_OPERATIONS = {"entrada", "saida"}


def calculate_balance(current: int, quantity: int, operation: str) -> int:
    """Calcula o novo saldo e rejeita movimentações incoerentes."""
    if current < 0 or quantity <= 0:
        raise ValueError("saldo e quantidade devem ser válidos")
    if operation not in VALID_OPERATIONS:
        raise ValueError("operação inválida")
    if operation == "saida" and quantity > current:
        raise ValueError("saída superior ao estoque disponível")
    return current + quantity if operation == "entrada" else current - quantity
