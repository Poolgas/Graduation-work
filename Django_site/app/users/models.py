from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """ORM модель пользователя для добавления дополнительных параметров пользователя"""
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True, null=True, verbose_name="Фотография")
    date_birth = models.DateTimeField(blank=True, null=True, verbose_name="Дата рождения")
