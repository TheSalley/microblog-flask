# -*- coding:utf-8 -*-
# @Author: TheShire
# @Time: 2023/1/13
# @File: routes.py
from app import app
from flask import render_template, flash, redirect, url_for
from app.form import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Alan'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Learn Python'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Learn JavaScript'
        },
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login request for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
