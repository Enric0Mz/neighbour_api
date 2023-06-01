import sqlalchemy as sa

from api.base_app.filters import comp_equals_filter_clause

from api.database.repository import Repository
from api.transactions import models
from api.transactions.entities.needs import NeedEntity


class NeedRepository(Repository):
    def to_dto(self, obj: NeedEntity) -> models.BaseNeed:
        return models.BaseNeed.parse_obj(
            {
                "description": obj.description,
                "period": obj.period,
            }
        )

    async def create(self, payload: models.BaseNeed):
        async with self.context.create_session() as session:
            need = NeedEntity(**payload.dict())

            session.add(need)
            await session.commit()

            return self.to_dto(need)

    async def fetch(self, filters: dict, page=0, limit=100):
        async with self.context.create_session() as session:
            f = comp_equals_filter_clause(NeedEntity, filters)

            q = (
                sa.select(NeedEntity)
                .where(*f)
                .limit(limit)
                .offset(page * limit)
            )

            result = await session.execute(q)

            return [self.to_dto(item) for item in result.scalars().all()]

    async def count(self):
        async with self.context.create_session() as session:
            q = sa.select(sa.func.count(NeedEntity.id)).where(
                NeedEntity.loan_id == None
            )

            result = await session.execute(q)

            return result.scalar_one()
