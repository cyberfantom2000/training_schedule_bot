import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from repository.baserepository import BaseRepository
from repository.sql import SqlRepository
from repository.models import SqlOrmBase


def create_repository(path: str) -> object:
    if not os.path.exists(path):
        open(path, 'w+').close()

    engine = create_engine('sqlite:///' + path)
    SqlOrmBase.metadata.create_all(engine)
    session = Session(bind=engine)
    return SqlRepository(BaseRepository(session))