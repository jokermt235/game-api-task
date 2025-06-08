from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Table, ForeignKey, Column,DateTime
from infrastructure.db import Base
from domain.user.models import User
from datetime import datetime

tournament_users = Table(
  "tournament_users",
  Base.metadata,
  Column("tournament_id", ForeignKey("tournaments.id"), primary_key=True),
  Column("user_id", ForeignKey("users.id"), primary_key=True),
)

class Tournament(Base):
  __tablename__ = "tournaments"

  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(String)
  max_players: Mapped[int] = mapped_column(Integer, nullable=False)
  start_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)

  users: Mapped[list[User]] = relationship(
    "User", secondary=tournament_users, back_populates="tournaments"
  )
