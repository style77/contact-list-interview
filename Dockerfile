FROM python:3.11:slim-buster

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libssl-dev \
    libffi-dev \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-wheel \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip pdm

WORKDIR /app

COPY pyproject.toml .

RUN pdm config python.use_venv False
RUN pdm install

COPY . .