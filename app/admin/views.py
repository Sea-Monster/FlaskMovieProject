# -*- coding: utf-8 -*-
from . import admin


# 调用蓝图
@admin.route('/')
def index():
    return 'this is admin'
