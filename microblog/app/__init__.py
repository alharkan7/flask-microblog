from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
<<<<<<< HEAD
from flask_login import LoginManager
=======
>>>>>>> master

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
<<<<<<< HEAD
login = LoginManager(app)
login.login_view = 'login'
=======
>>>>>>> master

from app import routes, models