# Mathgames Platform

MathgamesPlatformAPI - REST API, реализованный на Django REST Framework (DRF) с использованием PostgreSQL в качестве базы данных. В проекте реализовано два приложения:

*   Приложение-блог с аутентификацией пользователей через JWT-токен, позволяющее публиковать посты и комментарии. Для блога реализован небольшой фронтенд на Vue.js.
*   Реализация игры Hexapawn - пешечные шахматы Мартина Гарднера.
 

## Необходимые условия

*   Python 3.12+
*   Docker
*   Node.js 18+ (необязательно)

## Быстрый старт (Docker Compose)

Рекомендуемый способ запуска проекта - с использованием Docker Compose. Это обеспечит консистентность окружения и упростит процесс установки.

1.  **Клонируйте репозиторий:**

    ```bash
    git clone https://github.com/vncvtkv/MathgamesPlatformAPI.git
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
    docker compose up --build
    ```
    *   Эта команда автоматически запустит базу данных PostgreSQL, бэкенд Django и фронтенд Vue.js.
    *   Дождитесь завершения сборки и запуска контейнеров.

    ```bash
    docker exec -it mathgames_platform-backend-1 python manage.py migrate
    ```
    *   Выполните миграции.
    *   По адресу `http://localhost:8080` будет доступно небольшое фронтенд-приложение связанное с функционалом блога (или по адресу, указанному в логах фронтенда).

4.  **API Endpoints и примеры запросов:**

    Базовый функционал доступен на `http://localhost:8080`

    1. Аутентификация (Djoser + JWT)

        Базовый URL: http://localhost:8000/auth/

        **POST** `/users/ - Зарегистрировать нового пользователя<br>
        **POST**  /auth/jwt/create/ - Получить JWT-token


        #### Тело запроса при регистрации и получении токена:

        ```json
        {
        "username": "username",
        "password": "password"
        }

        ```



    ---

    2. Блог (CRUD операции)

        Базовый URL: http://localhost:8000/api/blog/

        **POST**	/post/	Создать новый пост (требуется auth)
        #### Тело запроса:

        ```json
        {
        "title": "title",
        "text": "text"
        }

        ```

        **GET**	   /post/{id}/	Получить конкретный пост<br>
        **POST**	/post/{id}/comment/	Добавить комментарий


    3. *Игра Hexapawn*

        Базовый URL: http://localhost:8000/api/game/

        **POST**	/hexapawn/	Создать новую игру<br>
        **POST**	/hexapawn/{game_id}/move/	Сделать ход<br>
        **GET**	/hexapawn/{game_id}/	Получить состояние игры


