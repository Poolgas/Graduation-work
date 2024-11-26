from datetime import datetime

from backend.db import Base
from sqlalchemy import Column, Integer, Text, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class Post(Base):
    """ Таблица SQLAlchemy "Статьи" """
    __tablename__ = 'posts'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    slug = Column(String, nullable=False)
    content = Column(Text)
    time_create = Column(DateTime, default=datetime.now())
    is_published = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=True, index=True, default=1)

    category = relationship('Category', back_populates='post')


class Category(Base):
    """ Таблица SQLAlchemy "Категории" """
    __tablename__ = 'category'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

    post = relationship('Post', back_populates='category')
