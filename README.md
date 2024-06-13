# Настройка и использование проекта

## Установка

1. Создайте виртуальное окружение:
    ```bash
    python3 -m venv .venv
    ```

2. Активируйте виртуальное окружение:
    ```bash
    source .venv/bin/activate
    ```

3. Установите зависимости:
    ```bash
    pip install -r requirements/base.txt
    ```

## Использование

1. Примените миграции:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

2. Создайте суперпользователя:
    ```bash
    python manage.py createsuperuser
    ```

3. Запустите сервер:
    ```bash
    python manage.py runserver
    ```

## Сборка и запуск проекта используя Докер

1. Запустите команду:
```
docker compose up -d --build
```