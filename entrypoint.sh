#!/bin/bash
set -e

# Активируем виртуальное окружение
source $(poetry env info -p)/bin/activate

# Ждем пока база данных будет доступна
echo "Waiting for database to be available..."
python wait_for_db.py # Или используйте другой способ дождаться БД

# Выполняем миграции
echo "Running migrations..."
python manage.py migrate

# Собираем статические файлы
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Запускаем сервер
echo "Starting server..."
python manage.py runserver 0.0.0.0:8000