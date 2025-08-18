FROM debian:latest

RUN apt update && apt install -y --no-install-recommends \
    chromium \
    curl \
    python3 \
    python3-pip \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /pdf

RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash && \
    bash -c "source /root/.nvm/nvm.sh && nvm install 22.18.0 && nvm use 22.18.0 && npm install puppeteer"

COPY makePdf.js /pdf/makePdf.js

WORKDIR /app

RUN curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/download/v3.4.17/tailwindcss-linux-arm64 && \
    chmod +x tailwindcss-linux-arm64 && \
    mv tailwindcss-linux-arm64 /tailwindcss

RUN python3 -m venv /venv

RUN /venv/bin/pip install --no-cache-dir \
    Markdown==3.7 \
    staticjinja==5.0.0 \
    watchdog==4.0.2
