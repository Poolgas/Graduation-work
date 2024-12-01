from typing import Annotated
from fastapi import APIRouter, Depends, status, HTTPException, Request, Form
from fastapi.responses import RedirectResponse

from repository.post import *
from routers.category import get_all_category
from schemas.post import *
from backend.db_depends import get_db
from sqlalchemy.orm import Session

from templates import templates

router = APIRouter(prefix='/post', tags=['post'])

"""Руты для статей"""


@router.get('/add_post')
async def add_post(request: Request, operations=Depends(get_all_category)):
    """GET функция. Обрабатывает страницу для добавления новой статьи"""
    return templates.TemplateResponse('post/add_post.html', {'request': request, 'categories': operations['category']})


@router.post('/add_post')
async def create_post(title: str = Form(), content: str = Form(), slug: str = Form(),
                      category_id: int = Form(), db: Session = Depends(get_db)
                      ):
    """POST функция. Добавляет статью в БД"""
    try:
        post_data = PostCreate(title=title, content=content, slug=slug, category_id=category_id)
        post = create_new_post(post=post_data, db=db)
        return RedirectResponse('/'), post
    except:
        return RedirectResponse('/post/add_post')


@router.get('/p/{id}')
async def get_post(id: int,
                   db: Annotated[Session, Depends(get_db)],
                   request: Request,
                   ):
    """GET функция. Возвращает статью по ID"""
    post = retreive_post(id=id, db=db)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Статья не найдена')
    return templates.TemplateResponse('post/post.html',
                                      {'request': request, "post": post})


@router.put('/p/{id}')
async def update_post(
        id: int,
        post: Annotated[PostUpdate, Depends()],
        db: Annotated[Session, Depends(get_db)]
):
    """PUT функция. Обновляет статью по ID"""
    post = post_update(id=id, post=post, db=db)
    if not post:
        raise HTTPException(detail=f'Статья под номером{id} не найдена')
    return {'message': f'Статья успешно изменена', 'post': post}


@router.delete('/p/{id}')
async def delete_post(
        id: int,
        db: Annotated[Session, Depends(get_db)]
):
    """DELETE функция. Удаляет статью по ID"""
    post = post_delete(id=id, db=db)
    if post.get('error'):
        raise HTTPException(detail=post.get('error'), status_code=status.HTTP_400_BAD_REQUEST)
    return {'message': f'Статья под номером {id} успешно удалена', 'post': post}
