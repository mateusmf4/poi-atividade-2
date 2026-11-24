FROM ghcr.io/astral-sh/uv:python3.13-trixie-slim
WORKDIR /app

COPY . /app
EXPOSE 8000

ENTRYPOINT ["uv", "run", "gunicorn", "-w", "1", "--threads", "8", "-b", "0.0.0.0:8000", "app:app"]