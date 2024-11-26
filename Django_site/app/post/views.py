from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from .models import *
from django.views.generic import CreateView, ListView


# Create your views here.

class Home(ListView):
    """Класс обработки главной страницы"""
    template_name = 'post/index.html'
    model = Post
    paginate_by = 3
    context_object_name = 'posts'

    def context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def about(request):
    context = {'title': 'О сайте',
               'text1': 'Это просто заглушка', }
    return render(request, 'post/about.html', context)


def contact(request):
    context = {'title': 'Контакты'}
    return render(request, 'post/contact.html', context)


def show_post(request, post_id):
    """Показ опубликованных статей"""
    post = get_object_or_404(Post, pk=post_id)
    data = {
        'title': post.title,
        'post': post,
    }
    return render(request, "post/post.html", data)


class AddPost(LoginRequiredMixin, CreateView):
    """Класс на добавление новых статей"""
    model = Post
    fields = '__all__'
    template_name = 'post/add_post.html'
    success_url = reverse_lazy('post:home')
    extra_context = {
        'title': 'Добавление статьи',
    }
