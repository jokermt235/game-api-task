import pytest
from unittest.mock import AsyncMock
from application.tournament.commands import RegisterTournamentCommand
from application.user.commands import CreateUserCommand
from schemas.tournament import TournamentCreateSchema
from schemas.user import UserCreateSchema
from domain.tournament.models import Tournament, User


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


@pytest.mark.asyncio
async def test_create_user_success():
    mock_repo = AsyncMock()
    user_dto = UserCreateSchema(name="Vini Jr", email="test1@mail.com")

    fake_user = User(id=1, **user_dto.dict())

    mock_repo.create.return_value = fake_user

    use_case = CreateUserCommand(repo=mock_repo)

    result = await use_case.execute(user_dto)

    assert result.name == "Vini Jr"
    assert result.email == "test1@mail.com"
