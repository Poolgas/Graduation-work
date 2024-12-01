from routers.posts import *
from templates import templates

router = APIRouter(
    prefix='/pages',
    tags=['Pages']
)

"""Руты для страниц заглушек"""


@router.get('/about')
def about(request: Request):
    return templates.TemplateResponse('post/about.html', {'request': request})


@router.get('/contact')
def contact(request: Request):
    return templates.TemplateResponse('post/contact.html', {'request': request})


@router.get('/none')
def contact(request: Request):
    return templates.TemplateResponse('post/None.html', {'request': request})
