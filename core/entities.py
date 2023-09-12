from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class Member:
    full_name: str
    id: Optional[int] = None
    short_name: Optional[str] = None
    link: Optional[str] = None


@dataclass
class Event:
    title: str
    location: str
    deadline: datetime
    maintainer: Member
    msg_id: int
    chat_id: int
    max_members: Optional[int] = None
    description: Optional[str] = None
    id: Optional[int] = None
    cost: Optional[int] = None
    members: Optional[list[Member]] = None


def create_member(full_name: str, idx: int, short_name: Optional[str] = None, link: Optional[str] = None):
    return Member(id=idx, full_name=full_name, short_name=short_name, link=link)


def create_event(title: str, location: str, deadline: datetime, maintainer: Member, msg_id: int, chat_id: int,
                 max_members: Optional[int] = None, description: Optional[str] = None,
                 idx: Optional[int] = None, cost: Optional[int] = None, members: Optional[Member] = None):
    return Event(title=title, location=location, deadline=deadline, maintainer=maintainer, msg_id=msg_id,
                 chat_id=chat_id, max_members=max_members, description=description, id=idx, cost=cost, members=members)
