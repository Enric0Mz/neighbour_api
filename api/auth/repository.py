import sqlalchemy as sa
from pydantic import EmailStr

from api.base_app import exc
from api.base_app.filters import comp_equals_filter_clause
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

    async def get_by_refresh(self, filters: dict) -> None:
        async with self.context.create_session() as session:

            f = comp_equals_filter_clause(UserEntity, filters)

            q = sa.select(UserEntity).where(*f)

            result = await session.execute(q)

            return result.scalars().one()

    async def update_access_token(self, filters: dict, token: str) -> None:
        async with self.context.create_session() as session:
            f = comp_equals_filter_clause(UserEntity, filters)
            
            q = (
                sa.update(UserEntity)
                .where(*f)
                .values(token=token)
            )

            await session.execute(q)
            await session.commit()

    async def update_refresh_token(self, filters: dict, token: str):
        async with self.context.create_session() as session:

            f = comp_equals_filter_clause(UserEntity, filters)

            q = (
                sa.update(UserEntity)
                .where(*f)
                .values(refresh_token=token)
            )

            await session.execute(q)
            await session.commit()
