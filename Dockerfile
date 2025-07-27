FROM python:3.12-slim-bookworm

RUN apt-get update && apt-get install -y --no-install-recommends -q curl && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Копируем только pyproject.toml и poetry.lock (если есть)
COPY pyproject.toml poetry.lock* ./

# Устанавливаем Poetry
RUN pip install -U poetry

# Устанавливаем зависимости (без корня проекта)
RUN poetry install --no-interaction --no-root

# Копируем все файлы проекта *ДО* запуска manage.py
COPY . .

# Активируем виртуальное окружение и запускаем manage.py
RUN poetry env info  # Узнаем путь к виртуальному окружению
RUN . $(poetry env info -p)/bin/activate && python manage.py collectstatic --noinput

# Копируем скрипт entrypoint
COPY entrypoint.sh .

# Задаем entrypoint
ENTRYPOINT ["./entrypoint.sh"]