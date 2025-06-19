from sqlalchemy import select 
from mainapp.database import async_session_maker 
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import update as sqlalchemy_update, delete as sqlalchemy_delete

from mainapp.models import Brands, Crosses, Countries

'''-------------БРЕНДЫ------------'''

class BrandsView:

    # Получение списка брендов
    @classmethod
    async def get_all_brands(cls):
        async with async_session_maker() as session: 
            query = select(Brands)
            result = await session.execute(query)
            return result.scalars().all()

    # Получение конкретного бренда
    @classmethod
    async def get_current_brand(self, id: int):
        async with async_session_maker() as session: 
            query = select(Brands).filter_by(id=id)
            result = await session.execute(query)
            brands = result.scalars().all()
            return brands

    # Добавление нового бренда
    @classmethod
    async def add_brand(self, **values):
        async with async_session_maker() as session:
            async with session.begin():
                new_instance = Brands(**values)
                session.add(new_instance)
                try:
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()
                    raise e
                return new_instance
            
    # Полное обновление бренда
    @classmethod
    async def put_brand(self, id: int, **values):
        async with async_session_maker() as session:
            async with session.begin():
                query_update = (
                sqlalchemy_update(Brands)
                .where(Brands.id == id)
                .values(**values)
                .execution_options(synchronize_session="fetch")
            )
            result = await session.execute(query_update)
            try:
                await session.commit()
            except SQLAlchemyError as e:
                await session.rollback()
                raise e
            return result
        
    @classmethod
    async def patch_brand(self, id: int, **values):
        async with async_session_maker() as session:
            async with session.begin():
                query_update = (
                sqlalchemy_update(Brands)
                .where(Brands.id == id)
                .values(**values)
                .execution_options(synchronize_session="fetch")
            )
            result = await session.execute(query_update)
            try:
                await session.commit()
            except SQLAlchemyError as e:
                await session.rollback()
                raise e
            return result
        
            
    # Удаление бренда
    @classmethod
    async def delete_current_brand(self, id: int):
        async with async_session_maker() as session: 
            query = select(Brands).filter_by(id=id)
            result = await session.execute(query)
            brand_to_delete = result.scalar_one_or_none()

            if not brand_to_delete:
                return None
            
            # Удаляем бренд
            await session.execute(
                sqlalchemy_delete(Brands).filter_by(id=id)
            )

            await session.commit()
            return id
            
    

'''-------------КРОССЫ------------'''


class CrossesView:

    # Получение списка кроссов
    @classmethod
    async def get_all_crosses(cls):
        async with async_session_maker() as session: 
            query = select(Crosses)
            result = await session.execute(query)
            crosses = result.scalars().all()
            return crosses   

    # Получение конкретного кросса
    @classmethod
    async def get_current_cross(cls, id: int):
        async with async_session_maker() as session: 
            query = select(Crosses).filter_by(id=id)
            result = await session.execute(query)
            crosses = result.scalars().all()
            return crosses

    # Добавление нового кросса
    @classmethod
    async def add_cross(cls, **values):
        async with async_session_maker() as session:
            async with session.begin():
                new_instance = Crosses(**values)
                session.add(new_instance)
                try:
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()
                    raise e
                return new_instance

    # Удаление кросса
    @classmethod
    async def delete_current_cross(cls, id: int):
        async with async_session_maker() as session: 
            query = select(Crosses).filter_by(id=id)
            result = await session.execute(query)
            cross_on_delete = result.scalar_one_or_none()

            if not cross_on_delete:
                return None
            
            # Удаляем кросс
            await session.execute(
                sqlalchemy_delete(Crosses).filter_by(id=id)
            )

            await session.commit()
            return id
            