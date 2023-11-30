from sqlalchemy.exc import IntegrityError


class BaseRepository:
    def __init__(self, session) -> None:
        self.session = session

    def add(self, orm_model) -> None:
        self.session.add(orm_model)
        self.commit()

    def get(self, orm_type, filters=()) -> list:
        query = self.session.query(orm_type).filter(*filters)
        return [i for i in query]

    def remove(self, orm_type, filters=()) -> None:
        orms = self.session.query(orm_type).filter(*filters)
        for orm in orms:
            self.session.delete(orm)
            self.session.commit()

    def commit(self) -> None:
        try:
            self.session.commit()
        except IntegrityError as err:
            self.session.rollback()
            raise err
