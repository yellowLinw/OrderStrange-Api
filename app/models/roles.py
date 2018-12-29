#!/usr/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime

from sqlalchemy import Column, Integer, String, TIMESTAMP, UniqueConstraint

from app.models.base import Base


class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    guard_name = Column(String(255), nullable=False)
    update_at = Column(TIMESTAMP, nullable=True, default=datetime.now, onupdate=datetime.now)
    create_at = Column(TIMESTAMP, nullable=True, default=datetime.now)

    __table_args__ = (
        UniqueConstraint('name', 'guard_name', name='uix_roles_name_guard_name'),
    )
