#!/usr/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime

from flask_bcrypt import generate_password_hash, check_password_hash
from sqlalchemy import (
    Column, Integer, String, Boolean, TIMESTAMP, text, ForeignKey
)

from app.models.base import Base, db


class Administrator(Base):
    __tablename__ = 'administrators'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    username = Column(String(60), nullable=False, unique=True)
    _password = Column('password', String(64), nullable=False)
    phone = Column(String(20), nullable=False, server_default='', index=True)
    avatar = Column(String(255), nullable=False, server_default="", comment="头像")
    is_active = Column(Boolean, nullable=False, server_default=text('1'), comment='是否启用')
    is_super = Column(Boolean, nullable=False, server_default=text('0'), comment='是否超级管理员')
    update_at = Column(TIMESTAMP, nullable=True, default=datetime.now, onupdate=datetime.now)
    create_at = Column(TIMESTAMP, nullable=True, default=datetime.now)

    role_id = Column(Integer, ForeignKey('roles.id'))
    role = db.relationship('Role',
                           backref=db.backref('administrators', lazy='dynamic'))

    _hidden = ['_password']

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self._password, raw)
