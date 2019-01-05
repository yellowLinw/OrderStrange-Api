#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# flask_migrate plugin
migrate = Migrate()

class Base(db.Model):
    # 模型不生成表
    __abstract__ = True

    _hidden = []

    def hide(self, *keys):
        """
        隐藏字段
        :param keys:
        :return:
        """
        for key in keys:
            del self.__dict__[key]
        return self

    def to_json(self):
        """
        转换json前自动去掉多余/隐藏属性,
        :return:
        """
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]

        for hide in self._hidden:
            del dict[hide]

        return dict

    @classmethod
    def findById(self, id):
        """
        根据id查询
        :param id: integer
        :return: object|None
        """
        return self.query.get(id)
