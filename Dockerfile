FROM python:3.12-slim-buster

# Устанавливаем Poetry (если не установлен в базовом образе)
# Можно найти актуальные команды установки Poetry на официальном сайте: https://python-poetry.org/docs/cli/
RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && curl -sSL https://install.python-poetry.org | python3 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем переменную окружения для Poetry, чтобы он добавил свой bin в PATH
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

# Копируем файлы конфигурации Poetry
COPY pyproject.toml poetry.lock* /app/

# Устанавливаем зависимости проекта с помощью Poetry
# --no-dev - не устанавливать зависимости для разработки
# --no-interaction - избегать интерактивных запросов
RUN poetry install --no-dev --no-interaction

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]