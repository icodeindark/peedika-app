from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

import secrets







app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Adjust the path as needed
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)



app.config['SECRET_KEY'] = secrets.token_hex(16)  # Generates a 32-character hex key

from . import models   # Import your models
