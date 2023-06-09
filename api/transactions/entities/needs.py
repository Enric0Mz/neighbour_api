import sqlalchemy as sa

from api.database.entity import Entity
from api.products.entity import ProductEntity
from api.register.entities.user import UserEntity

from .loans import LoanEntity


class NeedEntity(Entity):
    __tablename__ = "needs"

    description = sa.Column(sa.Text)
    period = sa.Column(sa.String(255))
    product_id = sa.Column(sa.Integer, sa.ForeignKey("products.id"))
    user_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"))
    loan_id = sa.Column(sa.Integer, sa.ForeignKey("loans.id"))

    product = sa.orm.relationship(ProductEntity)
    user = sa.orm.relationship(UserEntity)
    loan = sa.orm.relationship(LoanEntity)
