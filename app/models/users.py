#!/usr/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, text

from app.models.base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    nickname = Column(String(100), server_default="", unique=True)
    mobile = Column(String(20), server_default="", nullable=False)
    sex = Column(Boolean, nullable=False, server_default="0", comment="0未知 1男 2女")
    avatar = Column(String(255), nullable=False, server_default="", comment="头像")
    is_block = Column(Boolean, nullable=False, server_default=text("0"), comment='是否冻结')
    is_active = Column(Boolean, nullable=False, server_default=text('1'), comment='是否启用')
    last_logged_ip = Column(Integer, nullable=True, comment="上次登录IP")
    last_logged_at = Column(TIMESTAMP, nullable=True, comment="上次登录时间")
    create_at = Column(TIMESTAMP, nullable=True, default=datetime.now, onupdate=datetime.now)
    update_at = Column(TIMESTAMP, nullable=True, default=datetime.now)

    _fields = Base.load_all_data_field()
