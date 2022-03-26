"""
@Project ：Spider for imagebed-sm.ms 
@File    ：sql_select.py
@Date    ：2022/3/26 13:52 
"""
# -*- coding: UTF-8 -*-

from dao import sql_connect


def select_mysql(sql):
    conn = sql_connect.connect()
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        conn.commit()
        conn.close()

        return data
    except Exception as e:
        print('error occured on select' + sql)
        print(e)
        conn.close()
        conn.rollback()
