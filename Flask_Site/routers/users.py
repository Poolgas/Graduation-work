from flask import render_template, url_for, request, flash, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from backend.db import db
from flask import Blueprint
from models.user import User
from flask_login import login_user, login_required, current_user, logout_user

user_route = Blueprint('route', __name__)


@user_route.route('/login', methods=["POST", "GET"])
def login():
    """Авторизация пользователя по Логину и Паролю"""
    if current_user.is_authenticated:
        return redirect(url_for('users.profile'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('users.profile'))
        else:
            flash('Неверный логин или пароль')
    return render_template('users/login.html', title='Авторизация')


@user_route.route('/profile')
def profile():
    """Представления профиля пользователя """
    if current_user.is_authenticated:
        return render_template('users/profile.html', user=current_user)
    else:
        return redirect(url_for('users.login'))


@user_route.route('/registration', methods=['GET', 'POST'])
def registration():
    """Регистрация нового пользователя с проверкой на уникальность Email, логина И хеширование пароля"""
    if current_user.is_authenticated:
        return redirect(url_for('users.profile'))
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')

        user_email = User.query.filter_by(email=email).first()
        user_username = User.query.filter_by(username=username).first()
        if user_email:
            flash('Данный Email уже используется')
            return redirect(url_for('users.registration'))
        elif user_username:
            flash('Данный Логин уже используется')
            return redirect(url_for('users.registration'))
        else:
            new_user = User(username=username, email=email, password=generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            flash('Поздравляю! Вы успешно зарегистрировались.')
            return redirect(url_for('users.login'))
    return render_template('users/registration.html', title='Регистрация')


@user_route.route('/logout')
@login_required
def logout():
    """Выход из авторизации"""
    logout_user()
    return redirect(url_for('posts.index'))
