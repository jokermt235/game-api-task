from sqlalchemy.ext.asyncio import AsyncSession
from domain.tournament.models import Tournament, TournamentUser


class TournamentRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, tournament: Tournament) -> Tournament:
        self.session.add(tournament)
        await self.session.commit()
        await self.session.refresh(tournament)


class TournamentUserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, tournamentUser: TournamentUser) -> TournamentUser:
        self.session.add(tournamentUser)
        await self.session.commit()
        await self.session.refresh(tournamentUser)
