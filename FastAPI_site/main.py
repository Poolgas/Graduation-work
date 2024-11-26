from fastapi import FastAPI, APIRouter, Request, Depends
from fastapi.staticfiles import StaticFiles

from repository.post import post_list
from routers import posts, users, category
from pages.router import router as router_pages
from typing import Annotated
from sqlalchemy.orm import Session
from backend.db_depends import get_db
from templates import templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/')
async def get_all_posts(request: Request, db: Annotated[Session, Depends(get_db)]):
    """Главная страница"""
    posts = post_list(db=db)
    return templates.TemplateResponse('post/index.html',
                                      {'request': request, "posts": posts})

app.include_router(users.router)
app.include_router(posts.router)
app.include_router(category.router)
app.include_router(router_pages)
