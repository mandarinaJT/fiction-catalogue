from sqlalchemy import Column, String, Integer
from .database import Base
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class DbUser(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    