# bound-memory

Aplicação em flask que faz alocação de memória para cada requisição.

## Execução
```bash
uv run gunicorn -w 1 --threads 8 -b 0.0.0.0:8000 app:app
```