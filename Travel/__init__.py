from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)



app.config['SECRET_KEY'] = 'e052a800df4e2117da044c67726f0cf4c5505e7184902f58c278eb98ebbae3983b06907849133e90712837bdabc3c23510a08c9f28e0b6c3d596742f60b6d51c3b38807990e7511f8930a9dd7ffeb404980e6de493320c110c823552d1a92ed537'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

with app.app_context():
    db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.login_view = 'home_page'
login_manager.init_app(app)

from .models import User

@login_manager.user_loader 
def load_user(user_id):
    return User.query.get(int(user_id))

# from .auth import auth as auth_blueprint
# app.register_blueprint(auth_blueprint)

# from .routes import routes as main_blueprint
# app.register_blueprint(main_blueprint)

from Travel import routes