from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class Member:
    tg_id: int
    full_name: str
    id: Optional[int] = None
    short_name: Optional[str] = None
    link: Optional[str] = None
    events_ids: Optional[list[int]] = None
    administered_event_ids: Optional[list[int]] = None


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
    admins: Optional[list[Member]] = None
    messages: Optional[list[Message]] = None

