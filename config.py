#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Config():
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")

    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
