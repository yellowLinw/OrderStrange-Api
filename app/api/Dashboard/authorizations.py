#!/usr/bin/python3
# -*- coding: utf-8 -*-
from datetime import datetime

from flask import request, jsonify
from flask_jwt_extended import create_access_token

from app import Administrator, exception
from app.api.dashboard import dash
from forms.auth import LoginForm


@dash.route('/authorizations', methods=["POST"])
def login():
    form = LoginForm(request.form)
    user = Administrator.query.filter_by(username=form.username.data).first()

    if user and user.check_password(form.password.data):
        user.update(last_logged_at=datetime.now())

        access_token = create_access_token(identity=user, fresh=True)
    else:
        exception.not_found('用户名或密码错误')

    return jsonify({'access_token': access_token}), 200
