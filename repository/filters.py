from models import Member
from sqlalchemy import or_, and_

# TODO add base class filter by id


class MemberFilter:
    def __int__(self, filters: dict):
        self.ids = []
        self.tg_ids = []
        if 'id' in filters:
            self.ids.append(filters['id'])
        if 'ids' in filters:
            self.ids.append(i for i in filters['ids'])
        if 'tg_id' in filters:
            self.tg_ids.append(filters['tg_id'])
        if 'tg_ids' in filters:
            self.tg_ids.append(i for i in filters['tg_ids'])

    def get(self) -> list:
        filters = []
        if self.ids:
            filters.append(or_(*self.ids))
        if self.tg_ids:
            filters.append(or_(*self.tg_ids))

        return and_(*filters)


class EventFilter:
    def __int__(self):
        self.ids = []


class MessageFilters:
    def __init__(self):
        self.ids = []