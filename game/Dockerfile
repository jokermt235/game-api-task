FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    libpq-dev \
    libzbar-dev \
    apt-utils \
    gettext \
    python3-dev \
    libwebp-dev \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

RUN pip install poetry

WORKDIR /app

COPY game/. /app/

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi
