FROM python:3.12-slim

WORKDIR /app

COPY poetry.lock pyproject.toml .env ./

RUN python -m pip install --no-cache-dir poetry==1.8.3 \
    && poetry config virtualenvs.create false \
    && poetry install --without dev --no-interaction --no-ansi \
    && rm -rf $(poetry config cache-dir)/{cache,artifacts}


COPY crm ./crm
WORKDIR /app/crm
