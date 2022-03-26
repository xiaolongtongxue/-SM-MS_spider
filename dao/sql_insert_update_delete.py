"""
@Project ：Spider for imagebed-sm.ms 
@File    ：sql_insert_update_delete.py
@Date    ：2022/3/26 13:57 
"""
# -*- coding: UTF-8 -*-

from dao import sql_connect


def noselect_mysql(sql):
    conn = sql_connect.connect()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print("Error")
        print(e)
    conn.close()
