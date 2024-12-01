from flask import Flask

from models import User
from routers.posts import post_route
from routers.users import user_route
from flask_login import LoginManager
from backend.db import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '5b65322b28b1d3b7e0cfd8ac57c741414e918501'

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.init_app(app)

app.register_blueprint(post_route, name='posts')
app.register_blueprint(user_route, name='users')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
