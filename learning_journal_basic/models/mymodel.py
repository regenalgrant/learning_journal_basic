from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    Date,
)

from learning_journal_basic.models.meta import Base


class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode)
    body = Column(Unicode)
    category = Column(Unicode)
    tags = Column(Unicode)
    creation_date = Column(Date)
