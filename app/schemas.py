from pydantic import BaseModel, Field, Json
from typing import Any


class FindBase(BaseModel):
    body: dict
    header: dict

    class Config:
        orm_mode = True

