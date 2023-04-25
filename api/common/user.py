from pydantic import EmailStr

from api.base_app.model import BaseModel


class BaseUser(BaseModel):
    name: str
    surname: str
    email: EmailStr