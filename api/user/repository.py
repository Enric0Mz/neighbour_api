import sqlalchemy as sa

from api.database.repository import Repository
from api.register.entities.user import UserEntity
from api.base_app import exc

from . import models


class UsersRepository(Repository):
    def to_dto(self, obj: UserEntity) -> models.BaseUser:
        return models.BaseUser.parse_obj(
            {"name": obj.name, "surname": obj.surname, "email": obj.email}
        )

    async def get(self, clause):
        async with self._context.create_session() as session:
            q = sa.select(UserEntity).where(UserEntity.email == clause)

            result = await session.execute(q)
            if first := result.scalars().first():
                return self.to_dto(first)
            raise exc.not_found()

    async def update(self, clause, payload: models.BaseUser):
        async with self._context.create_session() as session:
            q = (
                sa.update(UserEntity)
                .where(UserEntity.email == clause)
                .values(**payload.dict(exclude_unset=True))
            )

            await session.execute(q)
            await session.commit()

    async def delete(self, clause):
        async with self._context.create_session() as session:
            q = sa.delete(UserEntity).where(UserEntity.email == clause)

            await session.execute(q)
            await session.commit()

    async def update_password(self, clause, password: str):
        async with self._context.create_session() as session:
            q = (
                sa.update(UserEntity)
                .where(UserEntity.email == clause)
                .values(password=password)
            )

            await session.execute(q)
            await session.commit()
