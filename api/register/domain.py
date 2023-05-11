from api.base_app.security.bcrypt import get_password_hash
from api.database.config import DBConnectionHandler

from . import models
from .repositories.condominium import CondominiumRepository
from .repositories.user import UsersRepository


class CreateUserUseCase:
    def __init__(
        self,
        condominium_id: int,
        context: DBConnectionHandler,
        payload: models.CreateUser,
    ) -> None:
        self._condominium_id = condominium_id
        self._repository = UsersRepository(context)
        self._payload = payload

    async def execute(self):
        return await self._repository.create(
            models.CommitUser(
                name=self._payload.name,
                surname=self._payload.surname,
                email=self._payload.email,
                password=get_password_hash(self._payload.password),
                condominium_id=self._condominium_id,
            )
        )


class InsertCondominiumUseCase:
    def __init__(
        self, context: DBConnectionHandler, payload: models.Condominium
    ) -> None:
        self._repository = CondominiumRepository(context)
        self._payload = payload

    async def execute(self):
        return await self._repository.create(models.Condominium(**self._payload.dict()))
