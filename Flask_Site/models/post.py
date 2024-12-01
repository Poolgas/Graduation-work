from datetime import datetime
from backend.db import db


class Post(db.Model):
    """Модель класса для создания Статей"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    time_create = db.Column(db.DateTime, default=datetime.now())
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

    def repr(self):
        return f'<Post {self.title}>'


class Category(db.Model):
    """Модель класса для создания Категорий"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    posts = db.relationship('Post', backref='category', lazy=True)

    def __repr__(self):
        return f'<Category {self.name}>'
