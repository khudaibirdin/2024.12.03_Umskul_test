import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine(os.getenv("DB_PATH"))

Session = sessionmaker(bind=engine)

class Base(DeclarativeBase): pass


def get_session():
    return Session()


def init_db():
    Base.metadata.create_all(bind=engine)