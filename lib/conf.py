"""
@Project ：Spider for imagebed-sm.ms 
@File    ：conf.py
@Date    ：2022/3/26 13:43 
"""
# -*- coding: UTF-8 -*-
def get_sqlinf():
    return {
        # 有关于MySQL服务连接的一堆配置
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "password": "123456",
        "database": "test"
    }
def get_downloadpos():
    return {
        # 文件的下载路径
        "pos": "E:\\test3\\"
    }
def get_re_rules():
    # 此处正则表达式似乎有点问题还望大佬指教
    return r'<img src="https://t.loli.net/?url=(.*?)&w=50&h=50">'
def get_http_head():
    return {
        "User-Agent":
            "xxxx",# 在此处添加自己的UA
        "cookie":
            "xxxx" # 在此处添加自己的cookie
    }