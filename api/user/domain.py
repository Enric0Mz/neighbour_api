from api.base_app import exc
from api.base_app.security.bcrypt import get_password_hash, verify_password
from api.database.config import DBConnectionHandler

from . import models
from .repository import UsersRepository


class GetSelfUserUseCase:
    def __init__(self, context: DBConnectionHandler, user: models.BaseUser) -> None:
        self._repository = UsersRepository(context)
        self._user = user

    async def execute(self):
        filters = {"email": self._user.email}

        return await self._repository.get(filters)


class UpdateUserUseCase:
    def __init__(
        self,
        context: DBConnectionHandler,
        user: models.BaseUser,
        payload: models.BaseUser,
    ) -> None:
        self._repository = UsersRepository(context)
        self._user = user
        self._payload = payload

    async def execute(self):
        await self._repository.update(self._user.email, self._payload)


class UpdatePasswordUseCase:
    def __init__(
        self,
        context: DBConnectionHandler,
        user: models.BaseUser,
        payload: models.UpdatePassword,
    ) -> None:
        self._repository = UsersRepository(context)
        self._user = user
        self._payload = payload

    async def execute(self):
        verify = verify_password(self._payload.old_password, self._user.password)

        if verify:
            password = get_password_hash(self._payload.new_password)
            await self._repository.update_password(self._user.email, password)
        raise exc.incorrect_password()


class DeleteUserUseCase:
    def __init__(self, context: DBConnectionHandler, user: models.BaseUser) -> None:
        self._repository = UsersRepository(context)
        self._user = user

    async def execute(self):
        await self._repository.delete(self._user.email)
