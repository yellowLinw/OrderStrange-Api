#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask

from app.api.Dashboard import dash

DEFAULT_APP_NAME = 'ORDER'

DEFAULT_MODULES = [
    (dash, '/dash')
]


def create_app():
    # 多对多
    app = Flask(DEFAULT_APP_NAME)
    setting_modules(app, DEFAULT_MODULES)

    return app


def setting_modules(app, modules):
    # 注册Blueprint模块
    for module, url_prefix in modules:
        app.register_blueprint(module, url_prefix=url_prefix)
