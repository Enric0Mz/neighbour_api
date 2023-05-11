import sqlalchemy as sa

from api.database.entity import Entity
from api.register.entities.condominium import CondominiumEntity


class UserEntity(Entity):
    __tablename__ = "users"

    name = sa.Column(sa.String(255))
    surname = sa.Column(sa.String(255))
    email = sa.Column(sa.String(255))
    password = sa.Column(sa.String(255))
    token = sa.Column(sa.String(255))
    refresh_token = sa.Column(sa.String(255))
    condominium_id = sa.Column(sa.Integer, sa.ForeignKey("condominium.id"))

    condominium = sa.orm.relationship(CondominiumEntity)
