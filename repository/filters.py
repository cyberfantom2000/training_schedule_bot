from repository.models import Member, Event, TelegramMessage
from sqlalchemy import or_, and_


class IdFilter:
    def __init__(self, filters: dict):
        self.ids = []
        self.tg_ids = []
        if 'id' in filters:
            self.ids.append(filters['id'])
        if 'ids' in filters:
            self.ids.append(i for i in filters['ids'])


class MemberFilter(IdFilter):
    def __init__(self, filters: dict):
        IdFilter.__init__(self, filters)

        if 'tg_id' in filters:
            self.tg_ids.append(filters['tg_id'])
        if 'tg_ids' in filters:
            self.tg_ids.append(i for i in filters['tg_ids'])

    def get(self) -> list:
        filters = []
        if self.ids:
            filters.append(Member.tg_id.in_(self.ids))
        if self.tg_ids:
            filters.append(Member.tg_id.in_(self.tg_ids))

        return filters


class EventFilter(IdFilter):
    def __init__(self, filters: dict):
        IdFilter.__init__(self, filters)

    def get(self) -> list:
        filters = []
        if self.ids:
            filters.append(Event.id.in_(self.ids))

        return filters


class MessageFilters(IdFilter):
    def __init__(self, filters: dict):
        IdFilter.__init__(self, filters)

    def get(self) -> list:
        filters = []
        if self.ids:
            filters.append(TelegramMessage.id.in_(self.ids))

        return filters
