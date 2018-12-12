#!/usr/bin/python3
# -*- coding: utf-8 -*-

from app.api.dashboard import dash


@dash.route('/')
def index():
    return 'dash'
