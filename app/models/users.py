#!/usr/bin/python3
# -*- coding: utf-8 -*-

from app import db


class User(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    nickname = db.Column(db.String(100), nullable=True, unique=True)
    mobile = db.Column(db.String(20), default="", nullable=False)
    sex = db.Column(db.Boolean, nullable=False, default=True, comment="1男 0女")
    avatar = db.Column(db.String(255), nullable=False, default="", comment="头像")
    is_block = db.Column(db.Boolean, nullable=False, default=False)
    last_logged_ip = db.Column(db.Integer, nullable=True, comment="上次登录IP")
    last_logged_at = db.Column(db.TIMESTAMP, nullable=True, comment="上次登录时间")
    create_at = db.Column(db.TIMESTAMP, nullable=True)
    update_at = db.Column(db.TIMESTAMP, nullable=True)
