# Standard imports
from typing import Dict


# SA imports
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=True)
    username = Column(String(50), unique=True, nullable=False)
    hpwd = Column(String(255), nullable=False)

    def __repr__(self) -> str:
         return f'User(username={self.username}, hpwd={self.hpwd})'
