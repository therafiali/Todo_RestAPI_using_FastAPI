from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    

