# MathgamesPlatformAPI

MathgamesPlatformAPI - REST API, реализованный на Django REST Framework (DRF) с использованием PostgreSQL в качестве базы данных. В проекте реализовано два приложения:

*   Приложение-блог с аутентификацией пользователей через JWT-токен, позволяющее публиковать посты и комментарии. Для блога реализован небольшой фронтенд на Vue.js.
*   Реализация игры Hexapawn - пешечные шахматы Мартина Гарднера.
 

## Необходимые условия

*   Python 3.12+
*   Docker
*   Node.js 18+

## Быстрый старт (Docker Compose)

Рекомендуемый способ запуска проекта - с использованием Docker Compose. Это обеспечит консистентность окружения и упростит процесс установки.

1.  **Клонируйте репозиторий:**

    ```bash
    git clone https://github.com/vncvtkv/MathgamesPlatformAPI.git
    cd MathgamesPlatformAPI
    ```

2.  **Настройте переменные окружения:**

    *   Скопируйте файл `.env.example` в `.env`:

        ```bash
        cp .env.example .env
        ```
        
        *   **Важно:** Сгенерируйте надежный секретный ключ Django для production-среды. Вы можете использовать команду `python -c "import secrets; print(secrets.token_urlsafe(50))"`.

3.  **Запустите приложение с помощью Docker Compose:**

    ```bash
    docker compose up --build
    ```
    *   Эта команда автоматически запустит базу данных PostgreSQL, бэкенд Django и фронтенд Vue.js.
    *   Дождитесь завершения сборки и запуска контейнеров.

    ```bash
    docker exec -it mathgamesplatformapi-backend-1 python manage.py migrate
    ```
    *   Выполните миграции.
    *   По адресу `http://localhost:8080` будет доступно небольшое фронтенд-приложение связанное с функционалом блога (или по адресу, указанному в логах фронтенда).

4.  **API Endpoints и примеры запросов:**

    Базовый функционал доступен на `http://localhost:8000`

    * Аутентификация (Djoser + JWT)

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

    * **Блог (CRUD операции)**

        Базовый URL: http://localhost:8000/api/blog/

        POST	/post/	**Создать новый пост (требуется auth)**
        #### Тело запроса:

        ```json
        {
        "title": "title",
        "text": "text"
        }

        ```

        GET	   /post/{id}/	**Получить конкретный пост**<br>
        POST	/post/{id}/comment/	**Добавить комментарий**


    * **Игра Hexapawn**

        Базовый URL: http://localhost:8000/api/game/

        POST	/hexapawn/	**Создать новую игру**<br>
        ```json
        {
        "title": "title",
        "text": "text"
        }

        ```
        POST	/hexapawn/{game_id}/move/	**Сделать ход**<br>
        ```json
        {
        "title": "title",
        "text": "text"
        }

        ```
        GET	/hexapawn/{game_id}/	**Получить состояние игры**


