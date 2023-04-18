import sqlalchemy as sa

from api.database.repository import Repository
from api.register.entities.user import UserEntity

from .. import models


class UsersRepository(Repository):
    def to_dto(self, obj: UserEntity) -> models.BaseUser:
        return models.BaseUser.parse_obj(
            {"name": obj.name, "surname": obj.surname, "email": obj.email}
        )

    async def get(self, clause):
        async with self._context.create_session() as session:
            q = sa.select(UserEntity).where(UserEntity.email == clause)

            result = await session.execute(q)
            return result.scalars().first()

    async def create(self, model: models.BaseUser):
        async with self._context.create_session() as session:
            user = UserEntity(**model.dict())
            session.add(user)
            await session.commit()

            return self.to_dto(user)
