from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from .models import *
from django.views.generic import CreateView, ListView, UpdateView, DeleteView


# Create your views here.

class Home(ListView):
    """Класс обработки главной страницы с настройкой пагинации"""
    template_name = 'post/index.html'
    model = Post
    paginate_by = 3
    context_object_name = 'posts'

    def context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def about(request):
    """Функция обработчик страницы /about"""
    context = {'title': 'О сайте',
               'text1': 'Это просто заглушка', }
    return render(request, 'post/about.html', context)


def contact(request):
    """Функция обработчик страницы /contact"""
    context = {'title': 'Контакты'}
    return render(request, 'post/contact.html', context)


def show_post(request, pk):
    """Функция обработчик страницы /post возвращает статью по id если она была найдена"""
    post = get_object_or_404(Post, pk=pk)
    data = {
        'title': post.title,
        'post': post,
    }
    return render(request, "post/post.html", data)


class AddPost(LoginRequiredMixin, CreateView):
    """Класс обработчик страницы /add_post добавляет новые статьи"""
    model = Post
    fields = '__all__'
    template_name = 'post/add_post.html'
    success_url = reverse_lazy('post:home')
    extra_context = {
        'title': 'Добавление статьи',
    }


class UpdatePost(UpdateView):
    """Класс обработчик страницы /add_post редактирует выбранную статью"""
    model = Post
    fields = ['title', 'description', 'image', 'category', 'is_published']
    template_name = 'post/add_post.html'
    success_url = reverse_lazy('post:home')
    title_page = 'Редактирование статьи'
    extra_context = {
        'title': 'Изменение статьи'
    }


class DeletePost(DeleteView):
    """Класс обработчик страницы /delete_post удаляет выбранную статью"""
    model = Post
    success_url = reverse_lazy('post:home')
    template_name = 'post/delete_post.html'
    extra_context = {
        'title': 'Удалить статью?'
    }
