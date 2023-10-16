from dataclasses import dataclass
from typing import Optional
from datetime import datetime

COMMON, MODERATOR, ADMINISTRATOR = range(0, 3)


@dataclass
class Member:
    tg_id: int
    full_name: str
    privilege_level: int = COMMON
    id: Optional[int] = None
    short_name: Optional[str] = None
    link: Optional[str] = None
    events_ids: Optional[list[int]] = None


@dataclass
class Message:
    msg_id: int
    chat_id: int
    id: Optional[int] = None


@dataclass
class Event:
    title: str
    location: str
    deadline: datetime
    maintainer: Member
    max_members: Optional[int] = None
    description: Optional[str] = None
    id: Optional[int] = None
    cost: Optional[int] = None
    members: Optional[list[Member]] = None
    messages: Optional[list[Message]] = None
