# -*- coding: utf-8 -*-

# #####################################
# @Author: Feyiz135
# @Time: 2017-05-07
# #####################################

"""
生成各种类型的随机数据
"""

import random
from datetime import date, datetime, timedelta
import string


def _gen_data(iterable, length, exc=None):
    """
    :param iterable: 数据源
    :param length: 输出字符串的长度
    :param exc: 排除以exc中的值开头的字符串
    :return: 字符串
    """
    s = ''
    while 1:
        s = random.choice(iterable)
        if exc and s.startswith(exc):
            continue
        break
    return s + ''.join([random.choice(iterable) for _ in range(length - 1)])


def gen_random_string(length=8):
    """
    返回一个由大小写字母、数字与下划线随机组成的字符串
    :param length: 字符串的长度
    :return:非数字开头的字符串
    """
    chars = string.ascii_letters + string.digits + "_"
    return _gen_data(chars, length, tuple(string.digits))


def gen_random_hex(length=8):
    """
    返回一个指定长度的随机十六进制数构成的字符串
    :param length: 长度
    :return: 十六进制字符串
    """
    return _gen_data(string.hexdigits, length, '0')


def gen_random_int(length=6):
    """
    返回一个指定长度的随机整数
    :param length:
    :return:
    """
    return int(_gen_data(string.digits, length, '0'))


def gen_random_bin(length=8):
    """
    返回一个指定长度的随机二进制数构成的字符串
    :param length:
    :return:
    """
    return _gen_data(['0', '1'], length, '0')


def gen_random_bool():
    """随机返回一个二进制数"""
    return random.randint(0, 1)


def gen_one_item(sequence):
    """随机返回序列中的一项"""
    return random.choice(sequence)


def gen_relative_date(days=1):
    """
    返回一个相对于今日的日期
    :param days:天数差
    :return: 年-月-日
    """
    return date.today() - timedelta(days=days)


def gen_relative_time(hours=1, minutes=2, seconds=3):
    """
    返回相对于此刻的时间
    :param hours: 小时差
    :param minutes: 分钟差
    :param seconds: 秒数差
    :return: 时:分:秒
    """
    return (datetime.now() - timedelta(hours=hours, minutes=minutes, seconds=seconds)).strftime('%X')


def gen_relative_datetime(days=0, hours=1, minutes=2, seconds=3):
    """
    返回相对于此时的一个时间点
    :param days: 天数差
    :param hours: 小时差
    :param minutes: 分钟差
    :param seconds: 秒数差
    :return: 年-月-日 时:分:秒
    """
    return (datetime.now() - timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)).strftime('%Y-%m-%d %H:%M:%S')


def gen_timestamp():
    """
    返回此时的时间戳
    :return: 长度为13位的int
    """
    return int(datetime.now().timestamp() * 1000)


def gen_random_plate_number():
    """返回一个随机的车牌"""
    REGION = ['京', '津', '冀', '晋', '蒙', '辽', '吉', '黑', '沪', '苏', '浙', '皖', '闽', '赣', '鲁', '豫', '鄂',
              '湘', '粤', '桂', '琼', '渝', '川', '黔', '滇', '藏', '陕', '甘', '青', '宁', '新']
    region = random.choice(REGION)
    city = random.choice(string.ascii_uppercase)
    number = random.sample(_gen_data(string.ascii_uppercase, 2) + _gen_data(string.digits, 3), 5)
    return region + city + "".join(number)


if __name__ == "__main__":
    print(gen_relative_time())
