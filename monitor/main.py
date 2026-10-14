import psutil, time, sys

duracao = int(sys.argv[1]) if len(sys.argv) > 1 else 60
print(f"{duracao=}")
output = sys.argv[2] if len(sys.argv) > 2 else "metricas.csv"
print(f"{output=}")

with open(output, "w") as f:
    f.write("time,cpu_pct,mem_pct,mem_mb,mem_active_mb\n")
    try:
        for t in range(duracao):
            cpu = psutil.cpu_percent(interval=1)
            mem = psutil.virtual_memory()
            print(f"{t=} {cpu=} {mem.percent=}")
            f.write(f"{t},{cpu},{mem.percent},{round(mem.used / 1024 / 1024)},{round(mem.active / 1024 / 1024)}\n")
            f.flush()
    except KeyboardInterrupt:
        pass
