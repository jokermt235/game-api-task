import pytest
from unittest.mock import AsyncMock
from application.tournament.commands import RegisterTournamentCommand
from schemas.tournament import TournamentCreateSchema
from domain.tournament.models import Tournament


@pytest.mark.asyncio
async def test_create_tournament_success():
    mock_repo = AsyncMock()
    dto = TournamentCreateSchema(
        name="Copa America", max_players=8, start_at="2025-06-10T12:00:00"
    )

    fake_tournament = Tournament(id=1, **dto.dict())

    mock_repo.create.return_value = fake_tournament

    use_case = RegisterTournamentCommand(repo=mock_repo)

    result = await use_case.execute(dto)

    assert result.name == "Copa America"
    assert result.max_players == 8
