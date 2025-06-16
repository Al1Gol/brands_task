from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, declared_attr

from mainapp.config import get_db_url

DATABASE_URL = get_db_url() # Создаем объект класса для формирования ссылки на БД
engine = create_async_engine(DATABASE_URL) # Асинхронное подключение к БД
async_session_maker = async_sessionmaker(engine, expire_on_commit=False) # Создание сессий