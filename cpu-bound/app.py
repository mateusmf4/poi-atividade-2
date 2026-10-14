import time
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify(status="ok")

@app.get("/calcular")
def calcular():
    iteracoes = int(request.args.get("iteracoes", 50000))

    inicio = time.perf_counter()

    acumulador = 0.0
    for i in range(1, iteracoes + 1):
        acumulador += (i ** 0.5) * 1.000001

    tempo_total_ms = (time.perf_counter() - inicio) * 1000
    return jsonify(
        iteracoes=iteracoes,
        resultado=round(acumulador, 2),
        tempo_total_ms=round(tempo_total_ms, 2),
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, threaded=True)