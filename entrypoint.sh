#!/bin/bash
set -e

# Активируем виртуальное окружение
. $(poetry env info -p)/bin/activate

# Выполняем миграции
echo "Running migrations..."
python manage.py migrate

# Запускаем сервер
echo "Starting server..."
python manage.py runserver 0.0.0.0:8000