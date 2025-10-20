from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/microblog.db'
app.config['SECRET_KEY'] = 'PD12345678'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

from app import routes, alquimias
from app.models import models

with app.app_context():
    db.create_all()
