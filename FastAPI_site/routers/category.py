from typing import Annotated

from fastapi import APIRouter, Depends, status, HTTPException

from repository.post import *
from schemas.post import *
from backend.db_depends import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix='/category', tags=['category'])

"""Руты катгорий"""


@router.post('/')
async def create_category(
        category: Annotated[CategoryCreate, Depends()],
        db: Annotated[Session, Depends(get_db)],
):
    """Создание категории"""
    category = category_create(category=category, db=db)
    return {
        'category': category
    }


@router.get('/')
async def get_all_category(db: Annotated[Session, Depends(get_db)]):
    category = category_list(db=db)
    """Вывод всех категорий"""
    return {
        'category': category
    }


@router.get('/{id}')
async def get_category(id: int,
                       db: Annotated[Session, Depends(get_db)]
                       ):
    """Получение категории по id """
    category = retreive_category(id=id, db=db)
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Категории  не существует')
    return {
        'category': category
    }


@router.delete('/{id}')
async def delete_category(
        id: int,
        db: Annotated[Session, Depends(get_db)]
):
    """Удаление категорий"""
    category = category_delete(id=id, db=db)
    if category.get('error'):
        raise HTTPException(detail=category.get('error'), status_code=status.HTTP_400_BAD_REQUEST)
    return {'message': f'Категория: {id} успешно удалена'}
