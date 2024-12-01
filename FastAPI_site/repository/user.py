from sqlalchemy import select, update
from sqlalchemy.orm import Session

from hashing import Hasher
from models.user import User
from schemas.user import UserCreate, UserUpdate, UserCheck

""" CRUD операции (Create, Read, Update, Delete) для пользователей"""


def create_new_user(user: UserCreate, db: Session):
    """Создание нового пользователя"""
    user = User(
        username=user.username,
        email=user.email,
        password=Hasher.get_password_hash(user.password),
        firstname=user.firstname,
        lastname=user.lastname,
        age=user.age
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def retreive_user(user: UserCheck, db: Session):
    """Получение пользователя по id"""
    user = db.query(User).filter(User.username == user.username and User.password == user.password)
    return user


def user_list(db: Session):
    """Получение списка пользователей"""
    users = db.query(User).filter(User.is_active == True).all()
    return users


def user_update(id: int, user: UserUpdate, db: Session):
    """Обновление изменяемых данных пользователя"""
    user_in_db = db.execute(select(User).where(id == User.id))
    if user_in_db is not None:
        user_db = db.execute(update(User).where(id == User.id).values(
            firstname=user.firstname,
            lastname=user.lastname,
            age=user.age,
        ))
        db.commit()
        return user_db
    else:
        return {"error": f'Пользователь под номером {id} не найден'}


def user_delete(id: int, db: Session):
    """Удаление пользователя"""
    user_in_db = db.query(User).filter(User.id == id)
    if not user_in_db.first():
        return {"error": f'Пользователь: {id} не найден'}
    user_in_db.delete()
    db.commit()
    return {'message': f'user {id} удалена'}
