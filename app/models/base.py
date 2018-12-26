#!/usr/bin/python3
# -*- coding: utf-8 -*-

from app import db


class Base(db.Model):
    # 模型不生成表
    __abstract__ = True

    # 字段
    _fields = []

    @classmethod
    def load_all_data_field(cls):
        """
        获取类自身所有数据表映射字段名
        :return:
        """
        if hasattr(cls, '__table__'):
            return [c.name for c in cls.__table__.columns]

    # 隐藏字段
    def hide(self, *keys):
        for key in keys:
            self._fields.remove(key)
        return self

    # 添加字段
    def append(self, *keys):
        for key in keys:
            self._fields.append(key)
        return self
