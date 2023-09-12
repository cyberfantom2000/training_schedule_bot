from repository.baserepository import BaseRepository


class Sql:
    def __init__(self, base_repo: BaseRepository):
        self.base_repo = base_repo
