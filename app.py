from flask import Flask, redirect, render_template, request, url_for

from services.stock import calculate_balance

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev-only-change-me"

products = {
    "Arroz 5 kg": {"quantity": 18, "validity": "05/2027", "minimum": 10},
    "Feijão 1 kg": {"quantity": 7, "validity": "02/2027", "minimum": 10},
    "Leite em pó": {"quantity": 2, "validity": "11/2026", "minimum": 5},
}

@app.get("/")
def index():
    contrast = request.args.get("alto_contraste") == "1"
    return render_template("index.html", contrast=contrast)

@app.get("/health")
def health():
    return {"status": "ok"}, 200

@app.route("/movimentacao", methods=["GET", "POST"])
def movimentacao():
    contrast = request.args.get("alto_contraste") == "1"
    error = None
    success = None
    if request.method == "POST":
        name = request.form.get("produto", "").strip()
        operation = request.form.get("operacao", "")
        try:
            quantity = int(request.form.get("quantidade", "0"))
            if name not in products:
                raise ValueError("produto não encontrado")
            products[name]["quantity"] = calculate_balance(
                products[name]["quantity"], quantity, operation
            )
            success = "Movimentação registrada com sucesso."
        except (TypeError, ValueError) as exc:
            error = str(exc)
    return render_template(
        "movimentacao.html", products=products, contrast=contrast,
        error=error, success=success
    )

@app.get("/estoque")
def estoque():
    contrast = request.args.get("alto_contraste") == "1"
    return render_template("estoque.html", products=products, contrast=contrast)

if __name__ == "__main__":
    app.run(debug=True)
