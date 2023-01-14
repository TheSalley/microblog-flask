# -*- coding:utf-8 -*-
# @Author: TheShire
# @Time: 2023/1/14
# @File: models.py

<<<<<<< HEAD
from app import db
=======
from app import d
>>>>>>> 900fb88a703aa98d2540d28abc965668335a0b8a


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), index=True, unique=True)
    email = db.Column(db.String(100), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f'<User {self.username}>'
