import sqlalchemy as sa

from api.database.config import DBConnectionHandler
from api.common.user import BaseUser

from .repository import ProductRepository


class ListProductsByUserUseCase:
    def __init__(self, context: DBConnectionHandler, user: BaseUser, params) -> None:
        self._repository = ProductRepository(context)
        self._user_id = user.id
        self._params = params

    async def execute(self):
        return await self._repository.fetch(
            self._user_id, 
            self._params.page, 
            self._params.limit
        )