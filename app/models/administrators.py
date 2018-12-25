#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask_bcrypt import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP

from app.models.base import Base


class Administrator(Base):
    __tablename__ = 'administrators'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    username = Column(String(60), nullable=False, unique=True)
    _password = Column('password', String(32), nullable=False)
    phone = Column(String(20), nullable=False, server_default='', index=True)
    avatar = Column(String(255), nullable=False, server_default="", comment="头像")
    is_active = Column(Boolean, nullable=False, server_default="1", comment='是否启用')
    is_super = Column(Boolean, nullable=False, server_default="0", comment='是否超级管理员')
    last_logged_ip = Column(Integer, nullable=True, comment='上次登录IP')
    last_logged_at = Column(TIMESTAMP, nullable=True)
    update_at = Column(TIMESTAMP, nullable=True)
    create_at = Column(TIMESTAMP, nullable=True)

    _fields = Base.load_all_data_field()

    @property
    def password(self):
        return self._password

    def set_password(self, password):
        self._password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self._password, password)
