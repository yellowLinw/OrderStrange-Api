#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask_jwt_extended import create_access_token, create_refresh_token

from config import Config, os


def access_token(identity, fresh=True):
    return {
        'access_token': Config.JWT_HEADER_TYPE + ' ' + create_access_token(
            identity=identity, fresh=fresh
        ),
        'refresh_token': Config.JWT_HEADER_TYPE + ' ' + create_refresh_token(identity=identity),
        'expires_in': int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES")) * 60,
        'refresh_in': int(os.getenv("JWT_REFRESH_TOKEN_EXPIRES")) * 60
    }
