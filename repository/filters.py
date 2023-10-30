from models import Member, Event, TelegramMessage
from sqlalchemy import or_, and_


class IdFilter:
    def __int__(self, filters: dict):
        self.ids = []
        self.tg_ids = []
        if 'id' in filters:
            self.ids.append(filters['id'])
        if 'ids' in filters:
            self.ids.append(i for i in filters['ids'])


class MemberFilter(IdFilter):
    def __int__(self, filters: dict):
        IdFilter.__int__(self, filters)

        if 'tg_id' in filters:
            self.tg_ids.append(filters['tg_id'])
        if 'tg_ids' in filters:
            self.tg_ids.append(i for i in filters['tg_ids'])

    def get(self) -> list:
        filters = []
        if self.ids:
            filters.append(or_(Member.id == i) for i in self.ids)
        if self.tg_ids:
            filters.append(or_(Member.tg_id == i) for i in self.tg_ids)

        return and_(*filters)


class EventFilter(IdFilter):
    def __int__(self, filters: dict):
        IdFilter.__int__(self, filters)

    def get(self) -> list:
        filters = []
        if self.ids:
            filters.append(or_(Event.id == i) for i in self.ids)

        return and_(*filters)


class MessageFilters(IdFilter):
    def __int__(self, filters: dict):
        IdFilter.__int__(self, filters)

    def get(self) -> list:
        filters = []
        if self.ids:
            filters.append(or_(TelegramMessage.id == i) for i in self.ids)

        return and_(*filters)
