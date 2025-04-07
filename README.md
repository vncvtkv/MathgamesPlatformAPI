# Mathgames Platform

Mathgames Platform - это платформа для математических игр, разработанная с использованием Django (бэкенд) и Vue.js (фронтенд).

## Необходимые условия

*   Python 3.12+
*   Node.js 18+
*   Docker

## Быстрый старт (Docker Compose)

Рекомендуемый способ запуска проекта - с использованием Docker Compose. Это обеспечит консистентность окружения и упростит процесс установки.

1.  **Клонируйте репозиторий:**

    ```bash
    git clone <repository_url>
    cd mathgames_platform
    ```

2.  **Настройте переменные окружения:**

    *   Скопируйте файл `.env.example` в `.env`:

        ```bash
        cp .env.example .env
        ```

    *   Отредактируйте файл `.env` и заполните его соответствующими значениями.  **Обязательно установите надежный секретный ключ Django!**

        ```
        POSTGRES_DB=mathgame_db         # Имя базы данных PostgreSQL
        POSTGRES_USER=mathgame_user       # Имя пользователя PostgreSQL
        POSTGRES_PASSWORD=StrongPassword123 # Пароль пользователя PostgreSQL
        POSTGRES_HOST=127.0.0.1          # Хост PostgreSQL (для Docker используйте 127.0.0.1)
        POSTGRES_PORT=5432             # Порт PostgreSQL
        SECRET_KEY=your_secret_key_here   # Секретный ключ Django (сгенерируйте надежный!)
        DEBUG=True                       # Режим отладки (установите False для production)
        ```

        *   **Важно:** Сгенерируйте надежный секретный ключ Django для production-среды. Вы можете использовать команду `python -c "import secrets; print(secrets.token_urlsafe(50))"`.
        *   **Важно:** Убедитесь, что в `.gitignore` есть строка `.env`.

3.  **Запустите приложение с помощью Docker Compose:**

    ```bash
    docker-compose up --build
    ```

    *   Эта команда автоматически запустит базу данных PostgreSQL, бэкенд Django и фронтенд Vue.js.
    *   Дождитесь завершения сборки и запуска контейнеров.
    *   Откройте приложение в браузере по адресу `http://localhost:8080` (или по адресу, указанному в логах фронтенда).

## Ручной запуск (без Docker)

Если вы предпочитаете запустить приложение вручную, выполните следующие шаги:

### 1. Запуск базы данных PostgreSQL

docker run --name my-postgres \
  -e POSTGRES_USER=mathgame_user\
  -e POSTGRES_PASSWORD=StrongPassword123 \
  -e POSTGRES_DB=mathgame_db   \
  -p 5432:5432 \
  -d postgres:13.10


### 2. Настройка и запуск бэкенда (Django)

1.  Перейдите в директорию проекта (если вы еще не там).

2.  Создайте и активируйте виртуальное окружение:

    ```bash
    python3 -m venv venv
    source venv/bin/activate   # Linux/macOS
    venv\Scripts\activate  # Windows
    ```

3.  Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4.  Примените миграции:

    ```bash
    python manage.py migrate
    ```

5.  Запустите сервер разработки:

    ```bash
    python manage.py runserver
    ```

    *   Убедитесь, что сервер Django запустился без ошибок и слушает на порту 8000 (или другом настроенном порту).

### 3. Настройка и запуск фронтенда (Vue.js)

1.  Перейдите в директорию `front`:

    ```bash
    cd front
    ```

2.  Установите зависимости:

    ```bash
    npm install
    ```

    или

    ```bash
    yarn install
    ```

3.  Запустите сервер разработки:

    ```bash
    npm run serve
    ```

    *   Убедитесь, что сервер Vue.js запустился без ошибок и слушает на порту 8080 (или другом настроенном порту).

### 4. Доступ к приложению

Откройте браузер и перейдите по адресу `http://localhost:8080` (или адресу, указанному в логах фронтенда).

## Настройка переменных окружения

В файле `.env` определены следующие переменные:

*   `POSTGRES_DB`: Имя базы данных PostgreSQL.
*   `POSTGRES_USER`: Имя пользователя PostgreSQL.
*   `POSTGRES_PASSWORD`: Пароль пользователя PostgreSQL.
*   `POSTGRES_HOST`: Хост PostgreSQL (для Docker используйте 127.0.0.1).
*   `POSTGRES_PORT`: Порт PostgreSQL.
*   `SECRET_KEY`: Секретный ключ Django.  **Не используйте секретный ключ по умолчанию в production!**
*   `DEBUG`: Режим отладки Django (установите `False` в production).

## Решение проблем

*   **Ошибка подключения к базе данных:** Убедитесь, что PostgreSQL запущен и доступен, а также что переменные окружения, связанные с базой данных, настроены правильно.
*   **Ошибка при установке зависимостей:** Проверьте, что у вас установлены необходимые версии Python и Node.js.
*   **CORS Error:** Убедитесь, что CORS настроен правильно в вашем Django-проекте (см. документацию django-cors-headers).

## Дополнительная информация

*   [Django Documentation](https://docs.djangoproject.com/en/4.2/)
*   [Vue.js Documentation](https://vuejs.org/)
*   [Docker Documentation](https://docs.docker.com/)
*   [Docker Compose Documentation](https://docs.docker.com/compose/)