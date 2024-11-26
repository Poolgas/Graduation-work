from sqlalchemy.orm import Session

from models.post import Post, Category
from schemas.post import PostCreate, PostUpdate, CategoryCreate
from sqlalchemy import select, update

""" CRUD operations (Create, Read, Update, Delete) для Статей и Категорий"""


def create_new_post(post: PostCreate, db: Session):
    """Создание новой статьи"""
    post = Post(
        title=post.title,
        content=post.content,
        category_id=post.category_id,
        slug=post.slug)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


def retreive_post(id: int, db: Session):
    """Получение статьи по id"""
    post = db.query(Post).filter(Post.id == id).first()
    return post


def post_list(db: Session):
    """Получение списка статей"""
    posts = db.query(Post).filter(Post.is_published == True).all()
    return posts


def post_update(id: int, post: PostUpdate, db: Session):
    """Обновление статьи по id"""
    post_in_db = db.execute(select(Post).where(id == Post.id))
    if post_in_db is not None:
        post_db = db.execute(update(Post).where(id == Post.id).values(
            title=post.title,
            content=post.content,
            slug=post.slug,
            category_id=post.category_id,
        ))
        db.commit()
        return post_db
    else:
        return {"error": f'Статья под номером {id} не найдена'}


def post_delete(id: int, db: Session):
    """Удаление пользователя по id"""
    post_in_db = db.query(Post).filter(Post.id == id)
    if not post_in_db.first():
        return {"error": f'Статья под номером {id} не найдена'}
    post_in_db.delete()
    db.commit()
    return {'message': f'Статья: {Post.title} удалена'}


def category_create(category: CategoryCreate, db: Session):
    """Создание новой категории"""
    category = Category(
        name=category.name
    )
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


def category_list(db: Session):
    """Получение списка категорий"""
    category = db.query(Category).all()
    return category


def retreive_category(id: int, db: Session):
    """Получение категории по id"""
    post = db.query(Category).filter(Category.id == id).first()
    return post


def category_delete(id: int, db: Session):
    """Удаление категории по id"""
    category_in_db = db.query(Category).filter(Category.id == id)
    if not category_in_db.first():
        return {"error": f'Категория под номером {id} не найдена'}
    category_in_db.delete()
    db.commit()
    return {'message': f'Категория {id} удалена', }
