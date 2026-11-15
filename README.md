# controle-doacoes-estoque
MVP web para controle de doações e estoque da Associação Comunitária Novo Caminho.

## Como executar

```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
flask --app app run
```

O MVP utiliza Flask e terá como núcleo o cadastro de produtos, movimentações de entrada e saída e consulta de estoque.

## Revisao tecnica

As regras de movimentacao foram isoladas em `services/stock.py`, permitindo testes unitarios independentes da interface. Entradas invalidas e saidas superiores ao saldo sao rejeitadas antes da persistencia.
