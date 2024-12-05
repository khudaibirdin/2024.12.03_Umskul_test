from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean

from internal.database import Base


class Users(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    telegram_id = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)

    score = relationship('Scores', back_populates='user')


class Scores(Base):
    __tablename__ = 'scores'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    telegram_id = Column(Integer, ForeignKey('users.telegram_id'), nullable=False)
    discipline = Column(String, nullable=False)
    score = Column(Integer, nullable=False)
    
    user = relationship('Users', back_populates='score')
