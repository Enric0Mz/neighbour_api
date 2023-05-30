import jwt
from jwt import DecodeError

from api.auth.repository import AuthRepository
from api.base_app import exc
from api.base_app.security.auth_handler import (JWT_ALGORITHM,
                                                JWT_REFRESH_SECRET,
                                                create_access_token,
                                                create_refresh_token)
from api.base_app.security.bcrypt import verify_password
from api.database.config import DBConnectionHandler
from api.register.models import BaseUser
from api.register.repositories.user import UsersRepository



class UserLoginUseCase:
    def __init__(
        self,
        context: DBConnectionHandler,
        email: str,
        password: str,
    ) -> None:
        self._email = email
        self._password = password
        self._context = context
        self._repository = UsersRepository(context)

    async def execute(self):
        info = await self._repository.get(self._email)

        if info is None:
            exc.not_found()
        if verify_password(self._password, info.password):
            access = await create_access_token(self._context, info.email, info.pk)
            refresh = await create_refresh_token(self._context, info.email, info.pk)
            return {
                "access_token": access["token"],
                "expires": access["expires"],
                "type": "Bearer",
                "refresh_token": refresh["refresh_token"],
            }
        exc.incorrect_password()


class UserRefreshSessionUseCase:
    def __init__(self, refresh_token: str, context: DBConnectionHandler) -> None:
        self._refresh_token = refresh_token
        self._repository = AuthRepository(context)
        self._context = context

    async def execute(self):
        try:
            token = jwt.decode(
                self._refresh_token, JWT_REFRESH_SECRET, algorithms=JWT_ALGORITHM
            )
        except DecodeError:
            raise exc.invalid_token()

        if token:
            await self._repository.get_by_refresh(self._refresh_token)

            access = await create_access_token(self._context, token["sub"], token["id"])
            refresh = await create_refresh_token(
                self._context, token["sub"], token["id"]
            )

            return {
                "access_token": access["token"],
                "expires": access["expires"],
                "type": "Bearer",
                "refresh_token": refresh["refresh_token"],
            }


class LogoutUseCase:
    def __init__(self, context: DBConnectionHandler, user: BaseUser) -> None:
        self._repository = AuthRepository(context)
        self._user = user

    async def execute(self):
        await self._repository.update_access_token(self._user.email, None)
        await self._repository.update_refresh_token(self._user.email, None)
