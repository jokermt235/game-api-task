from domain.tournament.models import Tournament, TournamentUser, User
from schemas.tournament import TournamentCreateSchema, UserRegisterSchema
from schemas.user import UserCreateSchema


def create_tournament(data: TournamentCreateSchema) -> Tournament:
    return Tournament(**data.dict())


def register_user(data: UserRegisterSchema) -> TournamentUser:
    return Tournament(**data.dict())


def create_user(data: UserCreateSchema) -> User:
    return User(**data.dict())
