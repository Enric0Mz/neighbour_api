import sqlalchemy as sa

from api.database.entity import Entity

from .condominium_type import CondominiumTypeEntity
from .enums import StateEnum


class CondominiumEntity(Entity):
    __tablename__ = "condominium"

    name = sa.Column(sa.String(255))
    street = sa.Column(sa.String(255))
    neighborhood = sa.Column(sa.String(255))
    city = sa.Column(sa.String(255))
    state = sa.Column(sa.Enum(StateEnum))
    cep = sa.Column(sa.String(255))
    type_id = sa.Column(sa.Integer, sa.ForeignKey("condominium_type.id"))

    type = sa.orm.relationship(CondominiumTypeEntity)
