# -*- coding:utf-8 -*-
# @Author: TheShire
# @Time: 2023/1/13
# @File: config.py
import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a secret string'
