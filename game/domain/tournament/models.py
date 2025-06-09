from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Table, ForeignKey, Column
from infrastructure.db import Base
from datetime import datetime
from sqlalchemy import TIMESTAMP

tournament_users = Table(
    "tournament_users",
    Base.metadata,
    Column("tournament_id", ForeignKey("tournaments.id"), primary_key=True),
    Column("user_id", ForeignKey("users.id"), primary_key=True),
)


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    tournaments: Mapped[list["Tournament"]] = relationship(
        "Tournament", secondary="tournament_users", back_populates="users"
    )


class Tournament(Base):
    __tablename__ = "tournaments"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    max_players: Mapped[int] = mapped_column(Integer, nullable=False)
    start_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=False)

    users: Mapped[list[User]] = relationship(
        "User", secondary=tournament_users, back_populates="tournaments"
    )
