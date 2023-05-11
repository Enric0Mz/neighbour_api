import re

from pydantic import EmailStr, validator

from api.base_app.model import BaseModel


class BaseUser(BaseModel):
    name: str
    surname: str
    email: EmailStr


class CreateUser(BaseUser):
    password: str

    @validator("password")
    def validate_password(cls, value: str):
        if len(value) < 8:
            raise ValueError("Password must be longer tha 8 digits")
        if not re.search("[A-Z]", value):
            raise ValueError("Password must have at least one upper digit")
        if not re.search("[0-9]", value):
            raise ValueError("Password must have ate lesat one number")
        if not re.search(r"[ `!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?~]", value):
            raise ValueError("Password must have at least one special digit")
        return value


class CommitUser(CreateUser):
    condominium_id: int


class CondominiumType(BaseModel):
    name: str


class Condominium(BaseModel):
    name: str
    street: str
    neighborhood: str
    city: str
    state: str
    cep: str


class CondominiumCreate(Condominium):
    type_id: int
