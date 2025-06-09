from domain.tournament.models import Tournament, TournamentUser
from domain.tournament.services import create_tournament
from infrastructure.tournament.repository import (
    TournamentRepository,
    TournamentUserRepository,
)
from schemas.tournament import TournamentCreateSchema
from schemas.user import UserCreateSchema


class RegisterTournamentCommand:
    def __init__(self, repo: TournamentRepository):
        self.repo = repo

    async def execute(self, data: TournamentCreateSchema) -> Tournament:
        tournament = create_tournament(data)
        await self.repo.save(tournament)
        return tournament


class RegisterUserCommand:
    def __init__(self, repo: TournamentUserRepository):
        self.repo = repo

    async def execute(self, data: UserCreateSchema) -> TournamentUser:
        tournament = create_tournament(data)
        await self.repo.save(tournament)
        return tournament
