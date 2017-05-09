# -*- coding: utf-8 -*-

# #####################################
# @Author: Feyiz135
# @Time: 2017-05-07
# #####################################

import re
from collections import namedtuple, OrderedDict
import pymysql
from .data_type import DataType


def desc_table(table):
    """
    获取表结构
    :param table: 表名
    :return: 字段名为键，字段约束为值的有序字典
    """
    Table = OrderedDict()
    Field = namedtuple('Constraint', ['type_', 'null', 'key', 'default', 'extra'])
    cur.execute("desc " + table)
    for row in cur:
        field_attr = Field._make(row[1:])
        field_name = row[0]
        Table[field_name] = field_attr
    return Table


def get_field_type(string_):
    """返回字段类型"""
    if string_.startswith('enum'):
        prefix = 'enum'
        start = string_.index('(')
        end = string_.rindex(')')
        length = string_[start + 1:end].split(',')
    else:
        try:
            index = string_.index('(')
        except ValueError:
            prefix = string_
            length = 0
        else:
            prefix = string_[:index]
            length = int(re.sub(r'\D', '', string_))
    return prefix, length


def gen_field_value(table):
    """
    设置字段的值
    :param table: 表名
    :return: 字段为key，字段的值为value的有序字典
    """
    field_value = OrderedDict()
    for field, constraint in desc_table(table).items():
        if constraint.default:
            field_value[field] = constraint.default
        elif constraint.null is 'YES':
            field_value[field] = ''
        else:
            field_type, length = get_field_type(constraint.type_)
            method = getattr(DataType, field_type)
            field_value[field] = method(length)
    return field_value


def gen_insert_sql(table):
    sql_prefix = "INSERT INTO " + table + " VALUES('{}'"
    sql_suffer = ");"

    d = gen_field_value(table)
    value = d.values()

    sql = sql_prefix + ",'{}'" * (len(value) - 1) + sql_suffer
    return sql.format(*value)


if __name__ == "__main__":
    conn = pymysql.connect(host='localhost', user='root', password='123456', database='roach', charset='utf8')  # 数据库连接串
    cur = conn.cursor()
    # print(gen_insert_sql('laneexlist'))
    for i in range(5000):
        cur.execute(gen_insert_sql('btclaneexlist'))
        if i % 100 == 0:
            conn.commit()
    cur.close()
    conn.commit()
    conn.close()
