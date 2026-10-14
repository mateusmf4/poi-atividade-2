# cpu-bound

Executa um loop N vezes, realizando operações matematicas

# Execução

```bash
uv run gunicorn -w 1 --threads 8 -b 0.0.0.0:8000 app:app
curl 'http://localhost:8000/calcular'
```