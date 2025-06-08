from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from infrastructure.db import Base

class User(Base):
  __tablename__ = "users"

  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(String)
  email: Mapped[str] = mapped_column(String)

  tournaments: Mapped[list['Tournament']] = relationship(
    'Tournament', secondary='tournament_users', back_populates='users'
  )