#!/usr/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime

from flask import request, jsonify
from flask_jwt_extended import (
    jwt_refresh_token_required, get_jwt_identity, fresh_jwt_required, get_raw_jwt
)

from app.api.dashboard import dash
from app.models.administratorLoginLogs import AdministratorLoginLog
from app.models.administrators import Administrator
from app.models.base import db
from common.exception import exception
from common.jwt import blacklist
from common.token import access_token
from forms.auth import LoginForm


@dash.route('/authorizations', methods=["POST"])
def login():
    form = LoginForm(request.form)
    user = Administrator.query.filter_by(username=form.username.data).first()

    if user and user.check_password(form.password.data):
        log = AdministratorLoginLog(
            user_agent=request.headers.get('User-Agent'),
            logged_ip=request.remote_addr,
            logged_at=datetime.now(),
            administrator=user
        )
        db.session.add(log)
        db.session.commit()

        data = access_token(identity=user.id)
    else:
        raise exception.not_found(message='用户名或密码错误')

    return jsonify({'data': data}), 200


@dash.route('/authorizations/refresh', methods=['PUT'])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()

    jti = get_raw_jwt()['jti']
    blacklist.add(jti)

    data = access_token(identity=current_user)

    return jsonify({'data': data}), 200


@dash.route('/authorizations/me', methods=['GET'])
@fresh_jwt_required
def me():
    user = Administrator.findById(get_jwt_identity()).to_json()

    return jsonify({'data': user}), 200
