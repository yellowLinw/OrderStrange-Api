#!/usr/bin/python3
# -*- coding: utf-8 -*-

from app.api.Dashboard import dash


@dash.route('/index')
def index():
    return 'dash'
