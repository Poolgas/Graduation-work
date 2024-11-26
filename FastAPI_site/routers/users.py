from fastapi import APIRouter, Depends, status, HTTPException, Request, Form
from sqlalchemy.orm import Session

from templates import templates
from backend.db_depends import get_db
from typing import Annotated
from fastapi.responses import RedirectResponse
from repository.user import create_new_user, user_list, retreive_user, user_update, user_delete
from schemas.user import *

router = APIRouter(prefix='/user', tags=['user'])
"""Руты для пользователей"""


@router.get('/')
async def all_users(db: Annotated[Session, Depends(get_db)]):
    """GET вывод всех пользователей"""
    users = user_list(db=db)
    return users


@router.get('/registration', response_class=RedirectResponse)
async def registration(request: Request):
    """GET для регистрации"""
    return templates.TemplateResponse('users/registration.html', {'request': request})


@router.post('/registration', status_code=status.HTTP_201_CREATED)
async def create_user(username: str = Form(), email: str = Form(), password: str = Form(),
                      firstname: str = Form(), lastname: str = Form(), age: int = Form(),
                      db: Session = Depends(get_db),
                      ):
    """POST для регистрации"""
    try:
        user_data = UserCreate(username=username, email=email, password=password,
                               firstname=firstname, lastname=lastname, age=age)
        user = create_new_user(user=user_data, db=db)
        return user, RedirectResponse('/user/login', status_code=302)
    except:
        return RedirectResponse('/user/registration', status_code=302)


@router.get('/login', response_class=RedirectResponse, status_code=302)
async def login(request: Request):
    """GET для аутентификации"""
    return templates.TemplateResponse('users/login.html', {'request': request})


@router.post('/login')
async def login_user(username: str = Form(), password: str = Form(), db: Session = Depends(get_db)):
    """POST для аутентификации"""
    try:
        user_data = UserCreate(username=username, password=password)
        user = retreive_user(user=user_data, db=db)
        return user, RedirectResponse('/user/profile', status_code=302)
    except:
        return RedirectResponse('/user/registration', status_code=302)


@router.get('/profile/{id}')
async def get_user(id: int,
                   db: Annotated[Session, Depends(get_db)],
                   ):
    """GET Вывод пользователя по id"""
    user = retreive_user(id=id, db=db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Пользователь не найден')
    return user


@router.put('/profile/{id}')
async def update_user(
        id: int,
        db: Annotated[Session, Depends(get_db)],
        user: Annotated[UserUpdate, Depends()],
):
    """PUT изменения данных пользователя по id"""
    user = user_update(id=id, user=user, db=db)
    if not user:
        raise HTTPException(detail=f'Пользователь: {id} не найден')
    return user


@router.delete('/profile/{id}')
async def delete_user(
        id: int,
        db: Annotated[Session, Depends(get_db)],
):
    """Delete пользователя по id"""
    user = user_delete(id=id, db=db)
    if user.get('error'):
        raise HTTPException(detail=user.get('error'), status_code=status.HTTP_400_BAD_REQUEST)
    return {'message': f'Пользователь: {id} успешно удален'}
