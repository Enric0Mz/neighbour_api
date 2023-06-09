import sqlalchemy as sa

from api.database.entity import Entity
from api.products.entity import ProductEntity
from api.register.entities.user import UserEntity


class LoanEntity(Entity):
    __tablename__ = "loans"

    loan_date = sa.Column(sa.DateTime)
    devolution_date = sa.Column(sa.DateTime)
    score = sa.Column(sa.Float(3, True, 1))
    avaliation = sa.Column(sa.Text)
    user_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"))
    product_id = sa.Column(sa.Integer, sa.ForeignKey("products.id"))

    user = sa.orm.relationship(UserEntity)
    product = sa.orm.relationship(ProductEntity)
