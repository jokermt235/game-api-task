from sqlalchemy.ext.asyncio import AsyncSession
from domain.tournament.models import User


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, user: User) -> User:
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
