from api.database.config import DBConnectionHandler
from api import common

from . import models
from .repositories.needs import NeedRepository


class CreateNeedUseCase:
    def __init__(self, context: DBConnectionHandler, user: common.BaseUser, product_id: int, payload: models.BaseNeed) -> None:
        self._repository = NeedRepository(context)
        self._user = user
        self._product_id = product_id
        self._payload = payload

    async def execute(self):
        return await self._repository.create(
            models.CreateNeed(
                **self._payload.dict(),
                product_id=self._product_id,
                user_id=self._user.id,
            )
        )