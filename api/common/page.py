from fastapi import Query
from pydantic import Field
from pydantic import validator
from pydantic.generics import GenericModel
from dataclasses import dataclass
from typing import Generic
from typing import TypeVar

from api.base_app.model import BaseModel


T_co = TypeVar("T_co", bound=BaseModel, covariant=True)


@dataclass(frozen=True)
class PageParams:
    page: int = Query(0)
    limit: int = Query(100)


class Details(BaseModel):
    page: int | None = None
    limit_per_page: int | None = None
    total_pages: int | None = 0
    total_items: int | None = None

    @validator("total_pages")
    def ensure_zero_on_none(cls, val: int | None):
        return 0 if val is None else val
    

class BasePagination(GenericModel, Generic[T_co], BaseModel):
    data: list = Field(default_factory=list)
    details: Details = Field(default_factory=Details)


