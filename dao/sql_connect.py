"""
@Project ：Spider for imagebed-sm.ms 
@File    ：sql_connect.py
@Date    ：2022/3/26 13:46 
"""
# -*- coding: UTF-8 -*-
import pymysql

from lib.conf import get_sqlinf

def connect(Servername=None, user=None, passwd=None, port=3306, database=None):
    if Servername is None or user is None or passwd is None or database is None:
        config = get_sqlinf()
    else:
        config = {
            "host": Servername,
            "port": port,
            "user": user,
            "password": passwd,
            "database": database
        }
    conn = pymysql.connect(**config)
    return conn