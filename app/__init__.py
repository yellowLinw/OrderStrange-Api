#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask

from app.api import *
from app.models.base import db, migrate
from common.exception import exception
from common.jwt import jwt
from config import Config

DEFAULT_APP_NAME = 'ORDER'

DEFAULT_MODULES = [
    (dash, '/dash')
]

def create_app(config=Config):
    app = Flask(DEFAULT_APP_NAME)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    exception.init_app(app)

    register_api_blueprint(app, DEFAULT_MODULES)

    return app


def register_api_blueprint(app, modules):
    # 注册Blueprint模块
    for module, url_prefix in modules:
        app.register_blueprint(module, url_prefix=url_prefix)