from django.db import models


# Create your models here.


class Category(models.Model):
    """Категории товаров"""
    name = models.CharField('Категория', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"


class Post(models.Model):
    """Модель для создания постов"""
    title = models.CharField("Название статьи", max_length=100)  # Название
    description = models.TextField("Описание", blank=True)  # Описание
    image = models.ImageField("Изображение", upload_to="Posts_image/", blank=True)  # Хранение изображений
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,
                                 verbose_name='Категория')  # Модель один ко многим для категорий
    time_update = models.DateTimeField(auto_now_add=True)  # Время изменения
    time_create = models.DateTimeField(auto_now=True)  # Время добавления
    is_published = models.BooleanField(verbose_name='Опубликовать', default=True)  # Опубликован ли пост
    objects = models.Manager()  # Менеджер по умолчанию

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]
