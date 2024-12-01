from typing import Optional

from pydantic import BaseModel, EmailStr, Field

""" Pydantic models (Schemas) для пользователей"""


class UserCreate(BaseModel):
    """Валидация данных для создания нового пользователя"""
    username: str = Field(
        min_length=3,
        max_length=50,
        example="Username",
        title="Имя пользователя",
        description="Минимум 3 символа, максимум 50.",
    )
    email: EmailStr = Field(
        example="Username@example.com",
        title="Электронная почта",
        description="Действительный адрес электронной почты.",
    )
    password: str = Field(min_length=5, max_length=50, description='Пароль, от 5 до 50 знаков')
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    age: Optional[int] = None


class UserUpdate(BaseModel):
    """Валидация данных для редактирования профиля"""
    id: int
    firstname: Optional[str]
    lastname: Optional[str]
    age: Optional[int]


class UserCheck(BaseModel):
    """Валидация данных для проверки наличия пользователя в БД"""
    id: int
    username: str
    password: str
