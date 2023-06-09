import sqlalchemy as sa

from api.base_app import exc
from api.base_app.filters import comp_equals_filter_clause
from api.database.repository import Repository
from api.register.entities.user import UserEntity

from . import models


class UsersRepository(Repository):
    def to_dto(self, obj: UserEntity) -> models.BaseUser:
        return models.BaseUser.parse_obj(
            {"name": obj.name, "surname": obj.surname, "email": obj.email}
        )

    async def get(self, filters: dict):
        async with self.context.create_session() as session:
            f = comp_equals_filter_clause(UserEntity, filters)

            q = sa.select(UserEntity).where(*f)

            result = await session.execute(q)
            if first := result.scalars().first():
                return self.to_dto(first)
            raise exc.not_found()

    async def update(self, clause, payload: models.BaseUser):
        async with self.context.create_session() as session:
            q = (
                sa.update(UserEntity)
                .where(UserEntity.email == clause)
                .values(**payload.dict(exclude_unset=True))
            )

            await session.execute(q)
            await session.commit()

    async def delete(self, clause):
        async with self.context.create_session() as session:
            q = sa.delete(UserEntity).where(UserEntity.email == clause)

            await session.execute(q)
            await session.commit()

    async def update_password(self, clause, password: str):
        async with self.context.create_session() as session:
            q = (
                sa.update(UserEntity)
                .where(UserEntity.email == clause)
                .values(password=password)
            )

            await session.execute(q)
            await session.commit()
