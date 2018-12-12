#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Blueprint

dash = Blueprint('dashboard', __name__)

from app.api.dashboard import index
