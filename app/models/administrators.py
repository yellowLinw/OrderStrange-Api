#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask_bcrypt import generate_password_hash, check_password_hash

from app import db


class Administrator(db.Model):
    __tablename__ = 'administrators'

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    username = db.Column(db.String(60), nullable=False, unique=True)
    password = db.Column(db.String(32), nullable=False)
    phone = db.Column(db.String(20), nullable=False, server_default='', index=True)
    avatar = db.Column(db.String(255), nullable=False, server_default="", comment="头像")
    is_active = db.Column(db.Boolean, nullable=False, server_default="1", comment='是否启用')
    is_super = db.Column(db.Boolean, nullable=False, server_default="0", comment='是否超级管理员')
    last_logged_ip = db.Column(db.Integer, nullable=True, comment='上次登录IP')
    last_logged_at = db.Column(db.TIMESTAMP, nullable=True)
    update_at = db.Column(db.TIMESTAMP, nullable=True)
    create_at = db.Column(db.TIMESTAMP, nullable=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
