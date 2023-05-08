from api.database.repository import Repository

from api.transactions.entities.needs import NeedEntity
from api.transactions import models


class NeedRepository(Repository):
    def to_dto(self, obj: NeedEntity) -> models.BaseNeed:
        return models.BaseNeed.parse_obj(
            {
                "description": obj.description,
                "period": obj.period,
            }
        )
    
    async def create(self, payload: models.BaseNeed):
        async with self.context.create_async_engine() as session:
            pass