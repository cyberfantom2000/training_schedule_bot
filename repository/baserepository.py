from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError


class BaseRepository:
    def __init__(self, session) -> None:
        self.session = session

    def add_and_commit(self, orm_model) -> None:
        try:
            self.session.add(orm_model)
            self.session.commit()
        except IntegrityError as err:
            self.session.rollback()
            raise err

    def create(self, orm_model) -> None:
        self.add_and_commit(orm_model)

    def get(self, orm_type, filters=()) -> list:
        query = self.session.query(orm_type).filter(or_(*filters))
        return [i for i in query]

    def remove(self, orm_type, orm_id) -> None:
        orm = self.session.query(orm_type).filter(orm_type.id == orm_id).first()
        if orm:
            self.session.delete(orm)
            self.session.commit()
