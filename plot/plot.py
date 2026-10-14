import sys
import pandas as pd
import matplotlib.pyplot as plt
import json
import numpy as np

ENTRADA = sys.argv[1]
ENTRADA_K6 = sys.argv[2]
SAIDA = sys.argv[3]
APP = 'mem'

def extrair_k6(caminho):
    with open(caminho) as f:
        dados = json.load(f)
    m = dados["metrics"]
    vus = int(m["vus_max"]["value"])
    dur = m["http_req_duration"]
    return f"{vus} usuários", dur["avg"], dur["p(90)"], dur["p(95)"], m["http_reqs"]["rate"]

for case in [1, 2, 3, 4]:
    for demanda in [5, 15, 30]:
        df = pd.read_csv(f'{ENTRADA}/case{case}/data_{APP}_{demanda}.csv')

        fig, ax = plt.subplots(figsize=(10, 5))

        ax.plot(df["time"], df["cpu_pct"], color="blue", linewidth=1.5, label="Uso de CPU (%)")
        ax.plot(df["time"], df["mem_pct"], color="red", linewidth=1.5, label="Uso de RAM (%)")

        ax.set_xlabel("Tempo (s)")
        ax.set_ylabel("Utilização (%)")
        ax.set_title(f"Provisionamento {case} - {demanda} usuários (Uso de CPU e RAM)")
        ax.set_ylim(0, 105)
        ax.grid(True, alpha=0.3)
        ax.legend(loc="best")

        out = f"{SAIDA}/{APP}_pro{case}_user{demanda:02}.png"
        fig.tight_layout()
        fig.savefig(out, dpi=150)
        print(f"Gráfico salvo em {out}")


    cenarios = [extrair_k6(f'{ENTRADA_K6}/case{case}/k6_{APP}_{c}.json') for c in [5, 15, 30]]
    rotulos = [c[0] for c in cenarios]
    valores = np.array([[c[1], c[2], c[3]] for c in cenarios])

    x = np.arange(len(rotulos))
    largura = 0.2
    espaco = 0.02
    series = ["Média", "p90", "p95"]
    cores = ["#2a78d6", "#eb6834", "#1baf7a"]

    fig, ax = plt.subplots(figsize=(10, 6))
    for i, (nome, cor) in enumerate(zip(series, cores)):
        barras = ax.bar(x + (i - 1) * (largura + espaco), valores[:, i], largura, label=nome, color=cor)
        ax.bar_label(barras, fmt="%.1f", padding=3, fontsize=9)

    ax.set_xticks(x)
    ax.set_xticklabels(rotulos)
    ax.set_xlabel("Demanda (usuários virtuais)")
    ax.set_ylabel("Tempo de resposta (ms)")
    ax.set_title(f"Provisionamento {case} (Tempo de resposta)")
    ax.set_axisbelow(True)
    ax.grid(axis="y", alpha=0.3)
    ax.legend()

    out = f"{SAIDA}/{APP}_pro{case}_resumo.png"
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    print(f"Gráfico salvo em {out}")

    vazoes = [c[4] for c in cenarios]
    x = range(len(rotulos))
    cor = plt.rcParams["axes.prop_cycle"].by_key()["color"][0]

    fig, ax = plt.subplots(figsize=(8, 6))
    barras = ax.bar(x, vazoes, width=0.5, color=cor, label="Vazão (req/s)")
    ax.bar_label(barras, fmt="%.1f", padding=3, fontsize=10)

    ax.set_xticks(list(x))
    ax.set_xticklabels(rotulos)
    ax.set_xlabel("Demanda (usuários virtuais)")
    ax.set_ylabel("Vazão (req/s)")
    ax.set_title(f"Provisionamento {case} (Vazão)")
    ax.set_axisbelow(True)
    ax.grid(axis="y", alpha=0.3)

    out = f"{SAIDA}/{APP}_pro{case}_vazao.png"
    fig.tight_layout()
    fig.savefig(out, dpi=150)