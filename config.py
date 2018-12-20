#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Config():
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
