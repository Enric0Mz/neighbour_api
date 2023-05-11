from typing import final

import sqlalchemy as sa
from sqlalchemy.orm import declared_attr

from .connection import Base


class Entity(Base):
    __abstract__ = True

    @final
    @declared_attr
    def id(self):
        return sa.Column(sa.Integer, primary_key=True, autoincrement=True)

    @property
    def pk(self):
        return self.id
