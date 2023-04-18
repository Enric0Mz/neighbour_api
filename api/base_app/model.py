from pydantic import BaseModel


class Model(BaseModel):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        frozen = True
