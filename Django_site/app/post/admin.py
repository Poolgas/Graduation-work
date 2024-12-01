from django.contrib import admin

from .models import Post, Category

# Register your models here.

admin.site.register(Category)


@admin.register(Post)
class ProductAdmin(admin.ModelAdmin):
    """Класс обработки админ панели для статей"""
    list_display = ('title', 'description', 'image', 'time_update', 'time_create', 'is_published')
    list_filter = ('title', 'category', 'is_published')
    search_fields = ('title', 'category')
    list_per_page = 20
    list_editable = ('is_published',)
    save_on_top = True
