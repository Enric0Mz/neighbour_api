from api.database.repository import Repository

from api.transactions.entities.loans import LoanEntity
from api.transactions import models


class LoanRepository(Repository):
    def to_dto(self, obj: LoanEntity) -> models.BaseLoan:
        return models.BaseLoan.parse_obj(
            {
                "id": obj.id,
                "loan_date": obj.loan_date,
                "devolution_date": obj.devolution_date,
            }
        )
    
    async def create(self, model: models.CreateLoan):
        async with self.context.create_session() as session:

            loan = LoanEntity(**model.dict())
            session.add(loan)
            await session.commit()

            return self.to_dto(loan)