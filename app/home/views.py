# -*- coding: utf-8 -*-
from . import home


# 调用蓝图
@home.route('/')
def index():
    return 'this is home'
