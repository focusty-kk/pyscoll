# -*- coding: utf-8 -*-
# 第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。

from learnpy.connect.mysql_init import *

import uuid

CODE_NUM = 200


def barncode():
    return [str(uuid.uuid1()).replace('-','').upper() for i in range(CODE_NUM)]

if __name__ == '__main__':
    mysql = mysql_init()
    mysql.connect()
    cur = mysql.cursor()
    codeArray = barncode()
    print(codeArray)
    cur.executemany('INSERT INTO code(code) VALUES(%s)', codeArray)
    mysql.commit()
    cur.close()
    mysql.close()


