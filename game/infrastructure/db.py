from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from fastapi import Depends
from config.settings import Settings
from config.deps import get_settings

engine_cache = {}

def get_engine(settings: Settings) -> any:
  if settings.database_url not in engine_cache:
    engine = create_async_engine(settings.database_url, echo=False)
    engine_cache[settings.database_url] = engine
  return engine_cache[settings.database_url]


def get_session(settings: Settings = Depends(get_settings)) -> AsyncSession:
  engine = get_engine(settings)
  session_maker = async_sessionmaker(engine, expire_on_commit=False)
  return session_maker()

class Base(DeclarativeBase):
  pass