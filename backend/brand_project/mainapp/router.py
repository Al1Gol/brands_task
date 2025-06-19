from fastapi import APIRouter
from sqlalchemy import select 
from mainapp.database import async_session_maker 
from mainapp.models import Brands, Crosses, Countries
from mainapp.views import BrandsView, CrossesView
from mainapp.schemas import SBrandAdd, SCrossAdd, SBrandPutUpdate, SBrandPatchUpdate

router = APIRouter(prefix='', tags=['Тестовое задание'])

'''-------------БРЭНДЫ------------'''

# Получение списка брендов
@router.get("/brands")
async def get_all_brands():
    return await BrandsView.get_all_brands()

# Получение конкретного бренда
@router.get("/brands/{id}")
async def get_current_brand(id: int):
    return await BrandsView.get_current_brand(id)

# Добавление нового бренда
@router.post("/brands")
async def add_brand(brand: SBrandAdd) -> dict:
    check = await BrandsView.add_brand(**brand.to_dict())
    if check:
        return {"message": "Бренд успешно добавлен!", "brand": brand}
    else:
        return {"message": "Ошибка при добавлении бренда!"}  

# Полное обновление бренда(PUT)
@router.put("/brands/{id}")
async def put_brand(id: int, new_data: SBrandPutUpdate) -> dict:
    check = await BrandsView.put_brand(id, **new_data.to_dict())
    if check:
        return {"message": "Бренд успешно обновлен!", "brand": new_data}
    else:
        return {"message": "Ошибка при обновлении бренда!"}  

# Частичное обновление бренда(PATCH)
@router.patch("/brands/{id}")
async def patch_brand(id: int, new_data: SBrandPatchUpdate) -> dict:
    # через exclude_none удаляем поля имеющие значение Null
    check = await BrandsView.patch_brand(id, **new_data.model_dump(exclude_none=True)) 
    if check:
        return {"message": "Бренд успешно обновлен!", "brand": new_data}
    else:
        return {"message": "Ошибка при обновлении бренда!"}  

# Удаление конкретного бренда
@router.delete("/brands/{id}")
async def get_current_brand(id: int):
    check = await BrandsView.delete_current_brand(id=id) 
    if check:
        return {"message": f"Бренд с ID {id} удален!"}
    else:
        return {"message": f"Ошибка при удалении бренда! Бренд с ID {id} отсутствует!"}
    
'''-------------КРОССЫ------------'''

# Получение списка кроссов
@router.get("/crosses")
async def get_all_crosses():
    return await CrossesView.get_all_crosses()

# Получение конкретного кросса
@router.get("/crosses/{id}")
async def get_current_crosses(id: int):
    return await CrossesView.get_current_cross(id)

# Добавление кросса
@router.post("/crosses")
async def add_cross(cross: SCrossAdd) -> dict:
    check = await CrossesView.add_cross(**cross.to_dict())
    if check:
        return {"message": "Кросс успешно добавлен!", "crosses": cross}
    else:
        return {"message": "Ошибка при добавлении кросса!"}  

# Получение конкретного кросса
@router.delete("/crosses/{id}")
async def get_current_crosses(id: int):
    check = await CrossesView.delete_current_cross(id=id) 
    if check:
        return {"message": f"Кросс с ID {id} удален!"}
    else:
        return {"message": f"Ошибка при удалении кросса! Бренд с ID {id} отсутствует!"}
