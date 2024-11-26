# Graduation-work
Дипломная работа на тему: Анализ и сравнение написания web-приложений с использованием Django, Flask, FastAPI.

Обзор проекта
Предлагается написать три простых веб приложения на базе фреймворков Django, FastAPI, Flask, провести анализ данных фреймворков и их сравнение. 
В качестве проекта, для всех трех фреймворков, была выбрана модель сайта-блога в котором пользователи могут выкладывать написанные ими статьи. 


На трех фреймворках использовались одинаковые шаблоны страниц.
base.html – Базовый шаблон, подключающий static файл, на его основании пишутся остальные. 
index.html – Главная страница с выводом всех статей на главный экран с датой публикации и категории.
about.html и contact.html - страницы заглушки в которых отсутствует backend функционал.

add_post.html - Страница добавления новой статьи.
post.html - Страница для показа конкретных статей.
update.html и delete.html - страницы обработки для изменения и удаления статей.
login.html – Вход в учётную запись
registration.html – Создание учётной записи
profile.html – Профиль пользователя.
Также используются Includes шаблоны которые в некоторых проектах не используются.
Header.html, footer.html и paginator.html - шаблоны для Header-а, footer-а и пагинации соответстенно.
Заключение
Приложения представляют функциональную основу для сайта-блога с возможностью расширения в будущем и добавлением дополнительного функционала. Все три приложения имеют схожую визуальную структуру но немного различающийся функционал.

Приложение 1. 
Пример файловой структуры для Django

│   db.sqlite3
│   manage.py
│
├───app
│   │   asgi.py
│   │   settings.py
│   │   urls.py
│   │   wsgi.py
│   └───__init__.py
│  
│
├───media
│   ├───post-image
│   │
│   └───users
│
├───post
│    │   admin.py
│    │   apps.py
│    │   forms.py
│    │   models.py
│    │   tests.py
│    │   urls.py
│    │   views.py
│    │   __init__.py
│    │
│    └───migrations
│        │   0001_initial.py
│        │   0002_alter_post_options_remove_post_slug_and_more.py
│        │   0003_alter_post_is_published.py
│        └───__init__.py
│
├───static
│    │
│    └───style.css
│    
├───templates
│   ├───includes
│   │  │   footer.html
│   │   │   header.html
│   │   └───paginator.html
│   ├───post
│   │  │   about.html
│   │  │   add_post.html
│   │  │   contact.html
│   │  │   index.html
│   │  └───post.htm
│   │  
|  ├───users
│   │  │   login.html
│   │  │   profile.html
│   │  └───registration.html
│   │     
│  ├───base.html
|
├───users
│    │   admin.py
│    │   apps.py
│    │   forms.py
│    │   models.py
│    │   tests.py
│    │   urls.py
│    │   views.py
│    │   __init__.py
│    │
│    └───migrations
│        │   0001_initial.py
│        └───__init__.py
Пример файловой структуры для Flask
│   main.py
│
├───backend
│   │   db.py
│   └─settings.py
│
├───instance
│   └───site.db
│
├───models
│    ├──  post.py
│    ├──   user.py
│    └───__init__.py
│
├───static
│   ├—  css 
│   │    └─ style.css
│   └─── images
│         └─ default.png
│   
├───templates
    ├───includes
    │  │   footer.html
    │  │   header.html
    │  └─paginator.html
    │  
    ├───post
    │  │   about.html
    │  │   add_post.html
    │  │   contact.html
    │  │   index.html
    │  │   delete.html
    │  │   update.html
    │  └─post.html
    │  
    ├───users
    │  │   login.html
    │  │   profile.html
    │  └─registration.html
    │     
    └────base.html

Пример файловой структуры для FastAPI  
│   templates.py
│   main.py
│   hashing.py
│   FastAPI_site.db
│  alembic.ini
│
├───backend
│   │   db.py
│   └───db_depends.py
│
├───migrations
│   ├───versions
|   │   └───bfc5ae308418_initial_migration.py
│   │       env.py
│   │       README
│   └─── script.py.mako
│
├───models
│    │   post.py
│    │   user.py
│    └─  __init__.py
│
├───static
│   ├—  css 
│   │    └─ style.css
│   └─── images
│         └─ default.png

├───pages
│    └─router.py    
│   
├───repository
│    │   post.py
│    └─  user.py
│    
├───routers
│    │   category.py
│    │   posts.py
│    │   users.py
│    └─ __init__.py
│
├───schemas
│    │   post.py
│    └─ user.py
│
├───templates
    ├───includes
    │  │   footer.html
    │  │   header.html
    │  └─paginator.html
    │  
   ├───post
    │  │   about.html
    │  │   add_post.html
    │  │   contact.html
    │  │   delete.html
    │  │   None.html
    │  │   post.html
    │  │   index.html
    │  └───post.htm
    │  
   ├───users
    │  │   login.html
    │  │   profile.html
    │  └─registration.html
    │     
    └──base.html

Приложение 2. 
Список необходимых библиотек для Django:
asgiref==3.8.1
Django==5.1.3
pillow==11.0.0
sqlparse==0.5.2
tzdata==2024.2
Список необходимых библиотек для Flask
annotated-types==0.7.0
blinker==1.9.0
click==8.1.7
colorama==0.4.6
Flask==3.1.0
Flask-Login==0.6.3
Flask-SQLAlchemy==3.1.1
greenlet==3.1.1
itsdangerous==2.2.0
Jinja2==3.1.4
Mako==1.3.6
MarkupSafe==3.0.2
SQLAlchemy==2.0.36
typing_extensions==4.12.2
Werkzeug==3.1.3
Список необходимых библиотек для FastAPI
aiosqlite==0.20.0
alembic==1.14.0
annotated-types==0.7.0
anyio==4.6.2.post1
bcrypt==4.2.1
click==8.1.7
colorama==0.4.6
dnspython==2.7.0
email_validator==2.2.0
fastapi==0.115.5
greenlet==3.1.1
h11==0.14.0
idna==3.10
Jinja2==3.1.4
Mako==1.3.6
MarkupSafe==3.0.2
passlib==1.7.4
pydantic==2.10.1
pydantic_core==2.27.1
python-multipart==0.0.17
python-slugify==8.0.4
sniffio==1.3.1
SQLAlchemy==2.0.36
starlette==0.41.3
text-unidecode==1.3
typing_extensions==4.12.2
uvicorn==0.32.1
