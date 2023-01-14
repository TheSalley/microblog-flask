# -*- coding:utf-8 -*-
# @Author: TheShire
# @Time: 2023/1/13
# @File: microblog.py
from app import app, db
from app.models import User, Post

@app.shell_context_processors
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Post': Post,
    }