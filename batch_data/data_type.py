# -*- coding: utf-8 -*-

# #####################################
# @Author: Feyiz135
# @Time: 2017-05-07
# #####################################

from .gendata import *


class DataType:
    """
    MySql数据库的基本数据类型
    """
    @staticmethod
    def bit(m=1):
        return gen_random_bin(m)

    @staticmethod
    def blog(m=16):
        length = random.randint(1, m) if m else random.randint(1, 16)
        return gen_random_bin(length)

    longblog = blog

    @staticmethod
    def tinyint(m=1):
        m = min(10 ** m -1, 10)
        return random.randint(0, m)

    smallint = tinyint
    bigint = tinyint
    int = tinyint

    @staticmethod
    def decimal(m=8, d=2):
        max = 10 ** (m-d) - 1
        return random.uniform(0, max)

    float = decimal
    double = decimal

    @staticmethod
    def char(m=1):
        length = random.randint(1, m)
        return gen_random_string(length)

    varchar = char
    text = char

    @staticmethod
    def enum(m=None):
        if not m:
            raise ValueError("枚举值的默认值为空，赋值错误")
        return gen_one_item(m)

    @staticmethod
    def DATE(m=0):
        return gen_relative_date()

    @staticmethod
    def TIME(m=0):
        return gen_relative_time()

    @staticmethod
    def YEAR(m=0):
        return

    @staticmethod
    def datetime(m=0):
        return gen_relative_datetime()

    @staticmethod
    def timestamp(m=0):
        return gen_timestamp()
