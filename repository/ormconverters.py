from core.entities import Member, Event, Message
from repository.models import Member as OrmMember
from repository.models import Event as OrmEvent
from repository.models import TelegramMessage as OrmMessage


def message_to_orm(message: Message, _=None) -> OrmMessage:
    return OrmMessage(id=message.id, msg_id=message.msg_id, chat_id=message.chat_id)


def message_from_orm(orm: OrmMessage) -> Message:
    return Message(id=orm.id, msg_id=orm.msg_id, chat_id=orm.chat_id)


def member_to_orm(member: Member, repository) -> OrmMember:
    events = __orm_events_or_empty(repository, member.events_ids)
    administered_events = __orm_events_or_empty(repository, member.administered_event_ids)

    return OrmMember(id=member.id, tg_id=member.tg_id, full_name=member.full_name,
                     link=member.link, short_name=member.short_name, events=events,
                     administered_events=administered_events)


def member_from_orm(orm: OrmMember) -> Member:
    return Member(id=orm.id, tg_id=orm.tg_id, full_name=orm.full_name,
                  short_name=orm.short_name, link=orm.link,
                  administered_event_ids=[event.id for event in orm.administered_events],
                  events_ids=[event.id for event in orm.events])


def event_to_orm(event: Event, repository) -> OrmEvent:
    return OrmEvent(id=event.id, location=event.location, deadline=event.deadline,
                    title=event.title, max_members=event.max_members,
                    description=event.description, cost=event.cost,
                    messages=[message_to_orm(message, repository) for message in event.messages],
                    members=[member_to_orm(member, repository) for member in event.members],
                    admins=[member_to_orm(admin, repository) for admin in event.admins])


def event_from_orm(orm: OrmEvent) -> Event:
    return Event(id=orm.id, location=orm.location, deadline=orm.deadline,
                 title=orm.title, max_members=orm.max_members,
                 description=orm.description, cost=orm.cost,
                 maintainer=member_from_orm(orm.maintainer),
                 messages=[message_from_orm(message) for message in orm.messages],
                 members=[member_from_orm(member) for member in orm.members],
                 admins=[member_from_orm(admin) for admin in orm.admins])


def update_member(orm: OrmMember, member: Member, _=None) -> None:
    orm.tg_id = member.tg_id
    orm.full_name = member.full_name
    orm.short_name = member.short_name
    orm.link = member.link


def update_event(orm: OrmEvent, event: Event, repository) -> None:
    orm.cost = event.cost
    orm.title = event.title
    orm.deadline = event.deadline
    orm.location = event.location
    orm.max_members = event.max_members
    orm.description = event.description
    orm.messages = [message_to_orm(message, repository) for message in event.messages]
    orm.members = [member_to_orm(member, repository) for member in event.members]
    orm.admins = [member_to_orm(admin, repository) for admin in event.admins]


def update_message(orm: OrmMessage, message: Message, _=None) -> None:
    orm.msg_id = message.msg_id
    orm.chat_id = message.chat_id


def __orm_events_or_empty(repository, ids: list) -> list:
    return repository.get(OrmEvent, [OrmEvent.id.in_(ids)]) if ids else []
