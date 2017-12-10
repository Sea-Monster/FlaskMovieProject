# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from app.models import Admin, Tag


class LoginForm(FlaskForm):
    """
    管理员登录表单
    """
    account = StringField(
        label='账号',
        validators=[
            DataRequired('请输入账号')
        ],
        description='账号',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入账号！',
            'required': 'required'
        }
    )

    pwd = PasswordField(
        label='密码',
        validators=[
            DataRequired('请输入密码！')
        ],
        description='密码',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入密码！',
            'required': 'required'
        }
    )

    submit = SubmitField(
        '登录',
        render_kw={
            'class': 'btn btn-primary btn-block btn-flat'
        }
    )

    def validate_account(self, field):
        """
        flask自动搜索Field名称（像这里的account，pwd，submit，以及默认的csrf_token），
        加上"validate_"前缀（例如validate_account）的方法名，如果存在该方法名，
        则该方法作为一个外部的验证方法
        :param field:
        :return:
        """
        account = field.data
        admin = Admin.query.filter_by(name=account).count()
        if admin == 0:
            raise ValidationError('账号不存在！')


class TagForm(FlaskForm):
    name = StringField(
        label='名称',
        validators=[
            DataRequired('请输入标签！')
        ],
        description='标签',
        render_kw={
            'class':'form-control',
            'id':'input_name',
            'placeholder':'请输入标签名称！'
        },
    )

    submit = SubmitField(
        '添加',
        render_kw={
            'class': 'btn btn-primary'
        }
    )