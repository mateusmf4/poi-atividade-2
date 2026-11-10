FROM ghcr.io/astral-sh/uv:python3.14-trixie-slim
WORKDIR /app

ENV UV_NO_DEV=1

COPY . /app
EXPOSE 8000

RUN uv sync --locked

CMD ["uv", "run", "gunicorn", "-w", "1", "--threads", "8", "-b", "0.0.0.0:8000", "app:app"]