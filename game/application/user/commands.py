from domain.tournament.models import User
from domain.tournament.services import create_user
from infrastructure.user.repository import UserRepository
from schemas.user import UserCreateSchema


class CreateUserCommand:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    async def execute(self, data: UserCreateSchema) -> User:
        user = create_user(data)
        await self.repo.save(user)
        return user
