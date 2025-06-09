from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    database_url: str = "sqlite+aiosqlite:///./game.db"
    log_db_url: str | None = None
    environment: str = "development"

    class Config:
        env_file = os.getenv("ENV_FILE", ".env")
