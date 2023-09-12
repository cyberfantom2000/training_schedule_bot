from sqlalchemy import Column, Integer, BigInteger, String, ForeignKey, DateTime, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

SqlOrmBase = declarative_base()


class EventToMember(SqlOrmBase):
    __tablename__ = 'eventtomember'
    member_id = Column(Integer, ForeignKey('members.id'), primary_key=True)
    event_id = Column(Integer, ForeignKey('events.id'), primary_key=True)


class Member(SqlOrmBase):
    __tablename__ = 'members'
    id = Column(BigInteger, primary_key=True)
    full_name = Column(String, nullable=False)
    short_name = Column(String)
    link = Column(String)
    events = relationship('Event', secondary='eventtomember')


class TelegramMessage(SqlOrmBase):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    msg_id = Column(Integer, nullable=False)
    chat_id = Column(BigInteger, nullable=False)
    event_id = Column(Integer, ForeignKey('messages.id'))
    event = relationship('Event', back_populates='messages')


class Event(SqlOrmBase):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    location = Column(String, nullable=False)
    deadline = Column(DateTime, nullable=False)
    cost = Column(BigInteger)
    message_id = Column(Integer, ForeignKey('messages.id'))
    message = relationship('TelegramMessage', back_populates='event')
    members = relationship('Member', secondary='eventtomember')
