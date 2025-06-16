from datetime import datetime
from typing import get_args

from sqlalchemy.sql import false, true, text
from sqlalchemy.orm import mapped_column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped

from sqlalchemy import Column, ForeignKey, Integer, SmallInteger, BigInteger, String, Text, Boolean, DateTime, Enum

CrossType = ['Локальный', 'ТекДок']

Base = declarative_base()

# создаем модель таблицы студентов
class Brands(Base):

    __tablename__ = 'brands'
    __tableargs__ = {'comment': 'brands'}

    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, server_default=str(datetime.now))
    updated_at = Column(DateTime, server_default=str(datetime.now), onupdate=datetime.now)
    name = Column(String)
    slug = Column(String)
    priority = Column(SmallInteger, default=0, server_default=text('0'))
    portal_id = Column(BigInteger, nullable=True)
    description = Column(Text, nullable=True)
    description_en = Column(Text, nullable=True)
    trademark = Column(String, nullable=True)
    is_active = Column(Boolean, default=True, server_default=true())
    is_ban = Column(Boolean, default=False, server_default=false())
    has_contact = Column(Boolean, default=False, server_default=false())
    invisible_ws = Column(Boolean, default=False, server_default=false())
    trademark_is_active = Column(Boolean, default=False, server_default=false())

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name!r})"

    def __repr__(self):
        return str(self)

class Crosses(Base):

    __tablename__ = 'crosses'
    __tableargs__ = {'comment': 'crosses'}

    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    name = Column(String)
    slug = Column(String)
    is_copy = Column(Boolean, default=False, server_default=false())
    type = Column(Enum('Локальный', 'ТекДок', name='type'), server_default="Локальный")
    user_id = Column(Integer)
    brand_id = Column(Integer, ForeignKey("brands.id"))
    portal_id = Column(BigInteger, nullable=True)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name!r})"

    def __repr__(self):
        return str(self)

class Countries(Base):

    __tablename__ = 'countries'
    __tableargs__ = {'comment': 'countries'}

    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    name = Column(String)
    slug = Column(String)
    portal_id = Column(BigInteger, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
    is_copy = Column(Boolean, default=True, server_default=true())

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name!r})"

    def __repr__(self):
        return str(self)
