from pydantic import BaseModel, Field, Json


class FindBase(BaseModel):
    body: dict
    header: dict

    class Config:
        orm_mode = True
