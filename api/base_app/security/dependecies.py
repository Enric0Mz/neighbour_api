import jwt
from fastapi import Request, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from api.auth.repository import AuthRepository
from api.database.config import DBConnectionHandler
from api.base_app import exc

from .auth_handler import JWT_SECRET
from .auth_handler import JWT_ALGORITHM


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)
        self._repository = AuthRepository(DBConnectionHandler())

    async def __call__(self, request: Request):
        try:
            credentials: HTTPAuthorizationCredentials = await super().__call__(request)
            if not credentials.credentials:
                raise exc.not_authenticated()

            user = jwt.decode(
                credentials.credentials, JWT_SECRET, algorithms=[JWT_ALGORITHM]
            )

            search_user = await self._repository.get_by_token(
                token=str(credentials.credentials)
            )

            if search_user is None:
                raise exc.not_authenticated()

            elif search_user.email == user["sub"]:
                return search_user
            raise exc.invalid_token()

        except jwt.DecodeError:
            raise exc.invalid_token()


protected_route = JWTBearer()
