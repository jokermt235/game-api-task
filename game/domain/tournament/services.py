from domain.tournament.models import Tournament
from schemas.tournament import TournamentCreateSchema

def create_tournament(data: TournamentCreateSchema) -> Tournament:
  return Tournament(**data.dict())