from core.entities import Member, Event, Message
from repository.models import Member as OrmMember
from repository.models import Event as OrmEvent
from repository.models import TelegramMessage as OrmMessage


def message_to_orm(message: Message, repository) -> OrmMessage:
    return OrmMessage(id=message.id, msg_id=message.msg_id, chat_id=message.chat_id)


def message_from_orm(orm: OrmMessage) -> Message:
    return Message(id=orm.id, msg_id=orm.msg_id, chat_id=orm.chat_id)


def member_to_orm(member: Member, repository) -> OrmMember:
    events = repository.get(OrmEvent, [OrmEvent.id == idx for idx in member.events_ids])
    return OrmMember(id=member.id, tg_id=member.tg_id, full_name=member.full_name,
                     link=member.link, short_name=member.short_name,
                     privilege_level=member.privilege_level, events=events)


def member_from_orm(orm: OrmMember) -> Member:
    return Member(id=orm.id, tg_id=orm.tg_id, full_name=orm.full_name,
                  short_name=orm.short_name, link=orm.link, privilege_level=orm.privilege_level,
                  events_ids=[event.id for event in orm.events])


def event_to_orm(event: Event, repository) -> OrmEvent:
    return OrmEvent(id=event.id, location=event.location, deadline=event.deadline,
                    title=event.title, max_members=event.max_members,
                    description=event.description, cost=event.cost,
                    messages=[message_to_orm(message, repository) for message in event.messages],
                    members=[member_to_orm(member, repository) for member in event.members])


def event_from_orm(orm: OrmEvent) -> Event:
    return Event(id=orm.id, location=orm.location, deadline=orm.deadline,
                 title=orm.title, max_members=orm.max_members,
                 description=orm.description, cost=orm.cost,
                 maintainer=member_from_orm(orm.maintainer),
                 messages=[message_from_orm(message) for message in orm.messages],
                 members=[member_from_orm(member) for member in orm.members])
