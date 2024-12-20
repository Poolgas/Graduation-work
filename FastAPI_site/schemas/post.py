from typing import Optional

from pydantic import BaseModel, Field

""" Pydantic models (Schemas) для статей """


class PostCreate(BaseModel):
    """Валидация данных для добавления новых статей"""
    title: str = Field(min_length=3,
                       max_length=50,
                       example="Статья про автомобили",
                       title="Название статьи",
                       description="Минимум 3 символа, максимум 50.",
                       )
    content: str = Field(title="Текст статьи")
    slug: Optional[str] = None
    category_id: Optional[int] = None


class PostUpdate(BaseModel):
    """Валидация данных для обновления статей"""
    id: int
    title: Optional[str] = None
    content: Optional[str] = None
    slug: Optional[str] = None
    category_id: Optional[int] = None


class CategoryCreate(BaseModel):
    """Валидация данных для добавления новой категории"""
    name: str
