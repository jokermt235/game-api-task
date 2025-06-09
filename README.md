# 🕹️ game-api

**FastAPI-сервис** для управления турнирами, построенный на асинхронном стеке: `FastAPI`, `SQLAlchemy`, `asyncpg`, `Alembic`.
Полностью контейнеризирован с помощью Docker.

---

## 🚀 Возможности

- FastAPI + Uvicorn + Gunicorn (ASGI)
- SQLAlchemy 2.0 (async)
- PostgreSQL
- Alembic для миграций
- Docker-окружение

---

## 🐳 Запуск в Docker

### 1. Cклонируйте проект

```bash
git clone https://github.com/jokermt235/game-api-task.git
cd game-api-task

docker-compose up --build


После запуска контейнера

зайти в game-manager container
docker exec -it game-manager /bin/sh

и запустить миграции если нужно сгенерить таблицы
alembic revision --autogenerate -m "initial"
alembic upgrade head

## LOCAL
Для  прогона  используй git хуки

pre-commit install

pre-commit run --all-files
