from sqlalchemy import Column, String, Integer, Date, ForeignKey, CheckConstraint, Enum
from sqlalchemy.orm import relationship
from .database import Base
from sqlalchemy.ext.declarative import declarative_base
import datetime
from db.schemas import media_type


Base = declarative_base()

class DbUser(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

class DbFiction(Base):
    __tablename__ = 'Fiction'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    author = Column(String(255), nullable=True)
    medium = Column(Enum(media_type), nullable=False)

    diary_entries = relationship("DbDiaryEntry", back_populates="fiction")

class DbDiaryEntry(Base):
    __tablename__ = 'DiaryEntries'
    id = Column(Integer, primary_key=True, index=True)
    score = Column(Integer, nullable=True)
    __table_args__ = (
        CheckConstraint('score >= 1 AND score <= 10', name='score_range'),
    )
    date = Column(Date, default=datetime.date.today)
    comment = Column(String(511), nullable=True)

    fiction_id = Column(Integer, ForeignKey("Fiction.id"), nullable=False)

    fiction = relationship("DbFiction", back_populates="diary_entries")