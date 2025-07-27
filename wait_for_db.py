import time
import psycopg2
import os

DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST", "db")  # По умолчанию db, если не указано иное
DB_PORT = os.environ.get("DB_PORT", 5432)


def wait_for_db():
    """Wait for the database to be available."""
    retries = 5
    for i in range(retries):
        try:
            conn = psycopg2.connect(
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                host=DB_HOST,
                port=DB_PORT,
            )
            conn.close()
            print("Database is available!")
            return True
        except psycopg2.OperationalError as e:
            print(f"Attempt {i + 1}/{retries}: Database not yet available: {e}")
            time.sleep(5)  # Подождем 5 секунд перед следующей попыткой
    print("Failed to connect to the database after multiple retries.")
    return False


if __name__ == "__main__":
    if not wait_for_db():
        exit(1)  # Выходим с ошибкой, если не удалось подключиться
