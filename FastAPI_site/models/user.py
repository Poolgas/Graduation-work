from backend.db import Base
from sqlalchemy import Column, Integer, String, Boolean


class User(Base):
    """ Таблица SQLAlchemy "Пользователи" """
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True)
    email = Column(String(100), unique=True)
    password = Column(String(500), nullable=False)
    firstname = Column(String(100), nullable=True, default='None')
    lastname = Column(String(100), nullable=True, default='None')
    age = Column(Integer, nullable=True, default=14)
    is_active = Column(Boolean, default=True)
