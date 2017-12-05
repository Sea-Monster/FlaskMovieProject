# -*- coding: utf-8 -*-
from . import home
from flask import render_template

# 调用蓝图
@home.route('/')
def index():
    return render_template('home/index.html')
