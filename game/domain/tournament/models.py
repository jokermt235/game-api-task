from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey
from infrastructure.db import Base
from datetime import datetime
from sqlalchemy import TIMESTAMP


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    tournament_users: Mapped[list["TournamentUser"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    tournaments: Mapped[list["Tournament"]] = relationship(
        secondary="tournament_users", back_populates="users", viewonly=True
    )


class Tournament(Base):
    __tablename__ = "tournaments"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    max_players: Mapped[int] = mapped_column(Integer, nullable=False)
    start_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=False)

    users: Mapped[list["User"]] = relationship(
        secondary="tournament_users", back_populates="tournaments", viewonly=True
    )

    tournament_users: Mapped[list["TournamentUser"]] = relationship(
        back_populates="tournament", cascade="all, delete-orphan"
    )


class TournamentUser(Base):
    __tablename__ = "tournament_users"

    tournament_id: Mapped[int] = mapped_column(
        ForeignKey("tournaments.id", ondelete="CASCADE"), primary_key=True
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), primary_key=True
    )

    tournament: Mapped["Tournament"] = relationship(back_populates="tournament_users")
    user: Mapped["User"] = relationship(back_populates="tournament_users")
