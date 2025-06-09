from pydantic import BaseModel
from datetime import datetime


class TournamentCreateSchema(BaseModel):
    name: str
    max_players: int
    start_at: datetime


class TournamentReadSchema(BaseModel):
    id: int
    name: str
    max_players: int
    start_at: datetime


class UserRegisterSchema(BaseModel):
    tournament_id: int
    user_id: int
