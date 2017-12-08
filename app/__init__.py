# -*- coding: utf-8 -*-
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@172.16.31.40:3306/movie'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = '随机CSRF的key'
app.debug=True

db = SQLAlchemy(app)

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

# 注册蓝图
app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix='/admin')

# 定义404页面
@app.errorhandler(404)
def page_not_found(error):
    return render_template('home/404.html'), 404