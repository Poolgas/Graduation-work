from datetime import datetime
from backend.db import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    """Модель класса для создания пользователя"""
    id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(500), nullable=True)
    created = db.Column(db.DateTime, default=datetime.now())
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<user {self.username}>'


