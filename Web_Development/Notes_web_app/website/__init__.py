# makes the website folder a python package 

from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)  # initializing flask 
    app.config['SECRET_KEY'] = "abcdefg"  # encrypt / secure cookies and session data related to website 
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # declaring where db is located and f is to use square bracket expressions 
    db.init_app(app) # initializing the database


    from .views import views  #registing blueprint/route of views
    from .auth import auth    #registing blueprint/route of auth

    app.register_blueprint(views,url_prefix='/') # registering blueprints of views
    app.register_blueprint(auth,url_prefix='/')  # registering blueprints of auth

    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print('Database created!')

