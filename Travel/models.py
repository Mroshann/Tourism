from flask_login import UserMixin
from . import db 

class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(length=60),nullable= False,unique=True)
    password = db.Column(db.String(length=60),nullable=False)
    username = db.Column(db.String(length=60),nullable=False)