# -*- coding: utf-8 -*-
from . import admin
from flask import render_template, redirect, url_for


# 调用蓝图
@admin.route('/')
def index():
    return render_template('admin/index.html')


# 登录
@admin.route('/login/')
def login():
    return render_template('admin/login.html')


# 退出
@admin.route('/logout/')
def logout():
    return redirect(url_for('admin.login'))

# 修改密码
@admin.route('/pwd/')
def pwd():
    return render_template('admin/pwd.html')