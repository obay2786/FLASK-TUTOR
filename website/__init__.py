from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'kunci rahasia'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mssql+pymssql://sa:Batam2021@103.142.240.134:1433/VMS'
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://sa:Batam2021@10.89.1.50:1433/VMS?driver=SQL+Server+Native+Client+11.0'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .models import User
    # db.drop_all(app=app)
    db.create_all(app=app)
    
    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app