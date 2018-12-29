#!/usr/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime

from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey

from app.models.base import Base, db
from common.ip2int import int2ip, ip2int


class AdministratorLoginLog(Base):
    __tablename__ = 'administrator_login_logs'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    user_agent = Column(String(255), nullable=True)
    _logged_ip = Column('logged_ip', Integer, nullable=True)
    logged_at = Column(TIMESTAMP, nullable=True, default=datetime.now)

    administrator_id = Column(Integer, ForeignKey('administrators.id'))
    administrator = db.relationship('Administrator',
                                    backref=db.backref('administrator_login_logs', lazy='dynamic'))

    @property
    def logged_ip(self):
        return self._logged_ip

    @logged_ip.getter
    def logged_ip(self):
        return int2ip(self._logged_ip)

    @logged_ip.setter
    def logged_ip(self, raw):
        self._logged_ip = ip2int(raw)
