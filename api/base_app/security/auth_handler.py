from typing import Optional
from pydantic import EmailStr
from datetime import datetime, timedelta

from decouple import config
import jwt

from api.database.config import DBConnectionHandler
from api.auth.repository import AuthRepository


JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")
JWT_REFRESH_SECRET = config("rsecret")


async def create_acess_token(
    context: DBConnectionHandler,
    email: EmailStr,
    user_id: str,
    expires_delta: Optional[timedelta] = None,
):
    current_timestamp = datetime.utcnow()
    if expires_delta:
        expire = current_timestamp + expires_delta
    else:
        expire = current_timestamp + timedelta(hours=100)
    encode = {"sub": email, "id": user_id, "exp": expire}
    token = jwt.encode(encode, JWT_SECRET, algorithm=JWT_ALGORITHM)
    await AuthRepository(context).update_acess_token(email, token)

    return {"token": token, "expires": expire, "type": "Bearer"}


async def create_refresh_token(
    context: DBConnectionHandler,
    email: EmailStr,
    user_id: str,
    expires_delta: Optional[timedelta] = None,
):
    current_timestamp = datetime.utcnow()
    if expires_delta:
        expire = current_timestamp + expires_delta
    else:
        expire = current_timestamp + timedelta(hours=100)
    encode = {"sub": email, "id": user_id, "exp": expire}
    jwtre = jwt.encode(encode, JWT_REFRESH_SECRET, algorithm=JWT_ALGORITHM)

    await AuthRepository(context).update_refresh_token(email, jwtre)

    return {"refresh_token": jwtre, "expires": expire, "type": "Bearer"}
