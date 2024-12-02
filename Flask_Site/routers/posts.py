from flask import render_template, url_for, request, flash, redirect
from flask import Blueprint
from flask_login import current_user

from backend.db import db
from models.post import Post, Category

post_route = Blueprint('route', __name__)


@post_route.route('/<int:page>')
@post_route.route('/')
def index(page=1):
    """Главная страница"""
    per_page = 3
    post_list = Post.query.paginate(page=page, per_page=per_page, error_out=False)
    return render_template('post/index.html', posts=post_list, title='Главная')


@post_route.route('/post/<int:post_id>')
def post(post_id):
    """Функция представления Статей"""
    post = Post.query.get_or_404(post_id)
    return render_template('post/post.html', post=post)


@post_route.route('/about')
def about():
    """Заглушка"""
    return render_template('post/about.html', title='О сайте')


@post_route.route('/contact')
def contact():
    """Заглушка"""
    return render_template('post/contact.html', title='Контакты')


@post_route.route('/add_post', methods=['GET', 'POST'])
def add_post():
    """Представление добавления новых статей"""
    if not current_user.is_authenticated:
        return redirect(url_for('users.login'))
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        category_id = request.form['category']
        post = Post(title=title, content=content, category_id=category_id)
        db.session.add(post)
        db.session.commit()
        flash('Статья добавлена!', 'success')
        return redirect(url_for('posts.index'))
    categories = Category.query.all()
    return render_template('post/add_post.html', categories=categories, tittle='Добавление записи')


@post_route.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def update_post(post_id):
    """Представление редактирования статей"""
    post = Post.query.get_or_404(post_id)
    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        post.category_id = request.form['category']
        db.session.commit()
        flash('Статья успешно обновлена!', 'success')
        return redirect(url_for('index'))
    categories = Category.query.all()
    return render_template('post/update.html', post=post, categories=categories)


@post_route.route('/delete_post/<int:post_id>', methods=['GET', 'POST'])
def delete_post(post_id):
    """Представление удаления статей"""
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Запись удалена!', 'success')
    return redirect(url_for('posts.index'))
