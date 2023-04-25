import sqlalchemy as sa

from api import common
from api.database.config import DBConnectionHandler
from api.common.user import BaseUser

from .repository import ProductRepository
from . import models


class ListProductsByUserUseCase:
    def __init__(self, context: DBConnectionHandler, user: BaseUser, params) -> None:
        self._repository = ProductRepository(context)
        self._user_id = user.id
        self._params = params

    async def execute(self):
        result = await self._repository.fetch(
            self._user_id, 
            self._params.page, 
            self._params.limit
        )

        total = await self._repository.count(self._user_id)

        total_pages = (
            0
            if (total / self._params.limit) == 1
            else (total // self._params.limit)
        )

        return common.BasePagination[models.Product](
            data=result,
            details=common.Details(
                page=self._params.page,
                limit_per_page=self._params.limit,
                total_pages=total_pages,
                total_items=total,
            ),
        )