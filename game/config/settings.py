from pydantic import BaseSettings
import os

class Settings(BaseSettings):
  database_url: str = "sqlite+aiosqlite:///./test.db"
  log_db_url: str | None = None
  environment: str = "development"

  class Config:
    env_file = os.getenv("ENV_FILE", ".env")