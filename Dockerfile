FROM ubuntu:latest

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    python3 \
    python3-pip \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/download/v3.4.17/tailwindcss-linux-arm64 && \
    chmod +x tailwindcss-linux-arm64 && \
    mv tailwindcss-linux-arm64 /tailwindcss

RUN python3 -m venv /venv

RUN /venv/bin/pip install --no-cache-dir \
    Markdown==3.7 \
    staticjinja==5.0.0 \
    watchdog==4.0.2
