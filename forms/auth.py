#!/usr/bin/python3
# -*- coding: utf-8 -*-

from wtforms import Form, StringField
from wtforms.validators import DataRequired, Length


class LoginForm(Form):
    username = StringField('用户名', validators=[
        DataRequired(message='用户名不可以为空'), Length(8, 20)
    ])
    password = StringField('密码', validators=[
        DataRequired(message='密码不可以为空'), Length(6, 20)
    ])
