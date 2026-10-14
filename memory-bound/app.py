import time
import resource
from flask import Flask, request, jsonify

app = Flask(__name__)

PAGE_SIZE = 4096
MAX_MB = 1024          # limite de segurança por requisição
MAX_TEMPO_MS = 10000   # limite de segurança para o tempo de retenção

# Usado pelo endpoint /reter para acumular memória entre requisições
RETIDO = []


def rss_mb():
    """Pico de memória residente do processo, em MB (Linux: ru_maxrss está em KB)."""
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/alocar")
def alocar():
    """
    Aloca `mb` megabytes, toca em todas as páginas (força a alocação física),
    mantém a memória ocupada por `tempo_ms` milissegundos e libera ao final.
    """
    mb = min(int(request.args.get("mb", 64)), MAX_MB)
    tempo_ms = min(int(request.args.get("tempo_ms", 100)), MAX_TEMPO_MS)

    inicio = time.perf_counter()

    buf = bytearray(mb * 1024 * 1024)      # bytearray já preenche com zeros, então toca as páginas
    for i in range(0, len(buf), PAGE_SIZE):  # escrita explícita, para garantir o uso físico
        buf[i] = 1

    time.sleep(tempo_ms / 1000)            # mantém a memória ocupada (simula trabalho)

    tempo_total_ms = (time.perf_counter() - inicio) * 1000
    return jsonify(
        alocado_mb=mb,
        tempo_retencao_ms=tempo_ms,
        tempo_total_ms=round(tempo_total_ms, 2),
        rss_pico_mb=round(rss_mb(), 2),
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, threaded=True)