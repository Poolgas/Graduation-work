from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator

from .models import Post


class AddPostForm(forms.ModelForm):
    """Форма создания новых постов по модели Post"""

    class Meta:
        model = Post
        fields = ['title', 'description', 'image', 'category', 'is_published']

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError("Длина превышает 50 символов")

        return title


class LoadFileForm(forms.Form):
    file = forms.FileField(label="Файл")
