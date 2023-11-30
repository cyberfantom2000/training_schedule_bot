from repository.baserepository import BaseRepository
from repository.ormconverters import (member_to_orm, member_from_orm, message_to_orm,
                                      message_from_orm, event_to_orm, event_from_orm,
                                      update_member, update_event, update_message)
from core.entities import Member, Event, Message
from repository.models import Member as OrmMember
from repository.models import Event as OrmEvent
from repository.models import TelegramMessage as OrmMessage


class SqlRepository:
    def __init__(self, base_repo: BaseRepository):
        self.base_repo = base_repo
        self.converters_to = {Member: member_to_orm, Event: event_to_orm, Message: message_to_orm}
        self.converters_from = {OrmMember: member_from_orm, OrmEvent: event_from_orm, OrmMessage: message_from_orm}
        self.updaters = {Member: update_member, Event: update_event, Message: update_message}
        self.mapping = {Member: OrmMember, Event: OrmEvent, Message: OrmMessage}

    def add(self, entities):
        orm = self._convert_to_orm(entities)
        self.base_repo.add(orm)

    def get(self, entities_type, filters):
        orms = self.base_repo.get(self.mapping[entities_type], filters.get())
        return [self._convert_from_orm(orm) for orm in orms] if orms else None

    def update_or_create(self, entities, filters):
        entities_type = type(entities)
        orms = self.base_repo.get(self.mapping[entities_type], filters.get())
        if orms:
            orm = orms[0]
            updater = self.updaters[entities_type]
            updater(orm, entities, self.base_repo)
            self.base_repo.commit()
        else:
            self.add(entities)

    def remove(self, entities_type, filters):
        self.base_repo.remove(self.mapping[entities_type], filters.get())

    def _convert_to_orm(self, entities):
        converter = self.converters_to[type(entities)]
        return converter(entities, self.base_repo)

    def _convert_from_orm(self, orm):
        converter = self.converters_from[type(orm)]
        return converter(orm)
