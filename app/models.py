from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.dialects.postgresql import JSONB
from .database import Base


class Find(Base):
    __tablename__ = "find"

    id = Column(Integer, primary_key=True)
    body = Column(JSONB)
    header = Column(JSONB)
    hash = Column(String)

    class Config:
        orm_mode = True
