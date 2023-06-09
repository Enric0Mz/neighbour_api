from api import common
from api.common.user import BaseUser
from api.database.config import DBConnectionHandler

from . import models
from .repository import ProductRepository


class ListProductsByUserUseCase:
    def __init__(self, context: DBConnectionHandler, user: BaseUser, params) -> None:
        self._repository = ProductRepository(context)
        self._user_id = user.id
        self._params = params

    async def execute(self):
        filters = {"user_id": self._user_id}

        result = await self._repository.fetch(
            filters, self._params.page, self._params.limit
        )

        total = await self._repository.count(filters)

        total_pages = (
            0 if (total / self._params.limit) == 1 else (total // self._params.limit)
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


class CreateProductUseCase:
    def __init__(
        self,
        context: DBConnectionHandler,
        user: BaseUser,
        paylaod: models.SimpleProduct,
    ) -> None:
        self._repository = ProductRepository(context)
        self._user_id = user.id
        self._payload = paylaod

    async def execute(self):
        return await self._repository.create(
            models.InsertProduct(**self._payload.dict(), user_id=self._user_id)
        )
