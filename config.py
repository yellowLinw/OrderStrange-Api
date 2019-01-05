#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
from datetime import timedelta

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Config():
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")

    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES")))
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(minutes=int(os.getenv("JWT_REFRESH_TOKEN_EXPIRES")))
    JWT_HEADER_TYPE = os.getenv("JWT_HEADER_TYPE")
    JWT_BLACKLIST_ENABLED = os.getenv("JWT_BLACKLIST_ENABLED")
    JWT_BLACKLIST_TOKEN_CHECKS = os.getenv("JWT_BLACKLIST_TOKEN_CHECKS")
