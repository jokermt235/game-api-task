from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from infrastructure.db import get_session
from infrastructure.tournament.repository import TournamentRepository
from app.tournament.commands import RegisterTournamentCommand
from schemas.tournament import TournamentCreateSchema, TournamentReadSchema
from domain.tournament.models import Tournament

router = APIRouter(prefix="/tournaments", tags=["tournaments"])


@router.post("/", response_model=TournamentReadSchema)
async def create_tournament_api(
    data: TournamentCreateSchema, session: AsyncSession = Depends(get_session)
) -> Tournament:
    repo = TournamentRepository(session)
    command = RegisterTournamentCommand(repo)
    tournament = await command.execute(data)
    return tournament
