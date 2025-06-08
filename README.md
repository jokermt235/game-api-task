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

### 1. Клонируйте проект

```bash
git clone https://github.com/jokermt235/game-api-task.git
cd game-api-task

docker-compose up --build
