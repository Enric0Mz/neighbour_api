import sqlalchemy as sa
from pydantic import EmailStr

from api.base_app import exc
from api.database.repository import Repository
from api.register.entities.user import UserEntity


class AuthRepository(Repository):
    async def get_by_token(self, token: str) -> None:
        async with self.context.create_session() as session:
            q = sa.select(UserEntity).where(UserEntity.token == token)

            result = await session.execute(q)

            if result:
                return result.scalars().first()
            raise exc.not_found()

    async def get_by_refresh(self, refresh: str) -> None:
        async with self.context.create_session() as session:
            q = sa.select(UserEntity).where(UserEntity.refresh_token == refresh)

            result = await session.execute(q)

            return result.scalars().one()

    async def update_acess_token(self, email: EmailStr, token: str) -> None:
        async with self.context.create_session() as session:
            q = (
                sa.update(UserEntity)
                .where(UserEntity.email == email)
                .values(token=token)
            )

            await session.execute(q)
            await session.commit()

    async def update_refresh_token(self, email: str, token: str):
        async with self.context.create_session() as session:
            q = (
                sa.update(UserEntity)
                .where(UserEntity.email == email)
                .values(refresh_token=token)
            )

            await session.execute(q)
            await session.commit()
