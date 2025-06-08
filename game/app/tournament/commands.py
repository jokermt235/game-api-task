from domain.tournament.models import Tournament
from domain.tournament.services import create_tournament
from infrastructure.tournament.repository import TournamentRepository
from schemas.tournament import TournamentCreateSchema

class RegisterTournamentCommand:
  def __init__(self, repo: TournamentRepository):
    self.repo = repo

  async def execute(self, data: TournamentCreateSchema) -> Tournament:
    tournament = create_tournament(data)
    await self.repo.save(tournament)
    return tournament