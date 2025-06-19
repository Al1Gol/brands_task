from datetime import datetime, date
from typing import Optional
import re
from pydantic import BaseModel, ConfigDict, Field

#Схема данных для добвления бренда
class SBrandAdd(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    slug: str
    priority: Optional[int] = None
    portal_id: int
    description: str
    description_en: str
    trademark: str
    is_active: Optional[bool] = None
    is_ban: Optional[bool] = None
    has_contact: Optional[bool] = None
    invisible_ws: Optional[bool] = None
    trademark_is_active: Optional[bool] = None

    #Представление данных в виде словаря
    def to_dict(self):
        return {
            "name": self.name,
            "slug": self.slug,
            "priority": self.priority,
            "portal_id": self.portal_id,
            "description": self.description,
            "description_en": self.description_en,
            "trademark": self.trademark,
            "is_ban": self.is_ban,
            "has_contact": self.has_contact,
            "invisible_ws": self.invisible_ws,
            "trademark_is_active": self.trademark_is_active,
        }
    

# Определение модели для новых данных бренда
class SBrandPutUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    slug: str
    priority: Optional[int] = None
    portal_id: int
    description: str
    description_en: str
    trademark: str
    is_active: Optional[bool] = None
    is_ban: Optional[bool] = None
    has_contact: Optional[bool] = None
    invisible_ws: Optional[bool] = None
    trademark_is_active: Optional[bool]  = None

    #Представление данных в виде словаря
    def to_dict(self):
        return {
            "name": self.name,
            "slug": self.slug,
            "priority": self.priority,
            "portal_id": self.portal_id,
            "description": self.description,
            "description_en": self.description_en,
            "trademark": self.trademark,
            "is_ban": self.is_ban,
            "has_contact": self.has_contact,
            "invisible_ws": self.invisible_ws,
            "trademark_is_active": self.trademark_is_active,
        }
    
# Определение модели для новых данных бренда
class SBrandPatchUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: Optional[str] = None
    slug: Optional[str] = None
    priority: Optional[int] = None
    portal_id: Optional[int] = None
    description: Optional[str] = None
    description_en: Optional[str] = None
    trademark: Optional[str] = None
    is_active: Optional[bool] = None
    is_ban: Optional[bool] = None
    has_contact: Optional[bool] = None
    invisible_ws: Optional[bool] = None
    trademark_is_active: Optional[bool] = None

    #Представление данных в виде словаря
    def to_dict(self):
        return {
            "name": self.name,
            "slug": self.slug,
            "priority": self.priority,
            "portal_id": self.portal_id,
            "description": self.description,
            "description_en": self.description_en,
            "trademark": self.trademark,
            "is_ban": self.is_ban,
            "has_contact": self.has_contact,
            "invisible_ws": self.invisible_ws,
            "trademark_is_active": self.trademark_is_active,
        }


#Схема данных для добвления кросссов
class SCrossAdd(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    slug: str
    is_copy: Optional[bool]
    type: Optional[str]
    user_id: int
    brand_id: int
    portal_id: int

    #Представление данных в виде словаря
    def to_dict(self):
        return {
            "name": self.name,
            "slug": self.slug,
            "is_copy": self.is_copy,
            "type": self.type,
            "user_id": self.user_id,
            "brand_id": self.brand_id,
            "portal_id": self.portal_id,
        }