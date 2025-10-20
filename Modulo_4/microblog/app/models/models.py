from app import db, login
from flask_login import UserMixin
from sqlalchemy.orm import relationship, Mapped
from datetime import datetime

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    remember = db.Column(db.Boolean, default=False)
    photo = db.Column(db.String(200))
    bio = db.Column(db.Text)
    last_login = db.Column(db.DateTime, default=datetime.now)

    posts: Mapped[list['Post']] = relationship(back_populates='author')

@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(500))
    timestamp = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    author: Mapped[User] = relationship(back_populates='posts')
