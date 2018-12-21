#!/usr/bin/python3
# -*- coding: utf-8 -*-

from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    nickname = db.Column(db.String(100), server_default="", unique=True)
    mobile = db.Column(db.String(20), server_default="", nullable=False)
    sex = db.Column(db.Boolean, nullable=False, server_default="0", comment="0未知 1男 2女")
    avatar = db.Column(db.String(255), nullable=False, server_default="", comment="头像")
    is_block = db.Column(db.Boolean, nullable=False, server_default="0", comment='是否冻结')
    is_active = db.Column(db.Boolean, nullable=False, server_default="1", comment='是否启用')
    last_logged_ip = db.Column(db.Integer, nullable=True, comment="上次登录IP")
    last_logged_at = db.Column(db.TIMESTAMP, nullable=True, comment="上次登录时间")
    create_at = db.Column(db.TIMESTAMP, nullable=True)
    update_at = db.Column(db.TIMESTAMP, nullable=True)
