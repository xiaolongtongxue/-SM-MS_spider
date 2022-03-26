"""
@Project ：Spider for imagebed-sm.ms 
@File    ：main.py
@Date    ：2022/3/26 13:43 
"""
# -*- coding: UTF-8 -*-
import argparse

from lib.conf import *
from dao.sql_insert_update_delete import noselect_mysql
from dao.sql_select import select_mysql
from util.download import download_
from util.re_name import re__

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument('-type', type=str, default=None)
    parser.add_argument('--value', type=str, default=None)
    parser.add_argument('--biantai', type=int, default=None)
    args = parser.parse_args()
    type = args.type
    if type is None:
        print("请传入参数，比如-type help")
        exit(0)
    elif type.lower() == "insert":
        value = args.value
        if value is not None:
            biantai = args.biantai
            if biantai == 0:
                if value[0:23] != "![](https://s2.loli.net":
                    print("url/dns error"+value)
                    exit(0)
                sql = "INSERT INTO `value`(inf,name) VALUES ('" + value[4:-1] + "','"+value[-20:-1]+"');"
                noselect_mysql(sql=sql)
            else:
                if value[0:19] != "https://s2.loli.net":
                    print("url/dns error"+value)
                    exit(0)
                sql = "INSERT INTO `value`(inf,name) VALUES ('" + value + "','"+value[-19:]+"');"
                noselect_mysql(sql=sql)
        else:
            print("接下来将自动补全数据库中的数据，开始爬取网页中的图片链接")
            import requests
            headers = get_http_head()
            req = requests.get(url="https://sm.ms/home/picture", headers=headers)
            if req.status_code >= 300:
                print("网站相应错误。错误码："+str(req.status_code))
                exit(0)
            html = req.content.decode('utf-8')
            values = re__(html, get_re_rules())
            for value in values:
                sql = "INSERT INTO `value`(inf,name) VALUES ('" + value + "','" + value[-19:] + "');"
                noselect_mysql(sql=sql)

    elif type.lower() == "select":
        sql = "SELECT * FROM `value`"
        data = select_mysql(sql)
        urls, names = [], []
        for i in data:
            urls.append(i[0])
            names.append(i[1])
        for i in range(len(urls)):
            print("url:"+urls[i]+" **--** names:"+names[i])
    elif type.lower() == "download":
        sql = "SELECT * FROM `value`"
        data = select_mysql(sql)
        urls, names = [], []
        for i in data:
            urls.append(i[0])
            names.append(i[1])
        for i in range(len(urls)):
            targetpath = get_downloadpos()['pos'] + names[i]
            download_(pos=targetpath, url=urls[i])
    elif type.lower() == "help":
        print("""
            关于本系统的使用：
            python main.py -type help
                输出帮助（本内容）
            python main.py -type select
                输出数据库中现有的全部url-name的键值对
            python main.py -type download
                将数据库中现有的全部键值对能下载的全部下载
            python main.py -type insert
                如果后边不加其他参数的话，目前功能尚未开发完善，此部分目的是将网站全部参数导入MySQL
            python main.py -type insert --biantai 0 --value "![](xx/autsKBEUobaujwT.png)"
                biantai参数的值为0的时候value的传参应当是markdown文档的格式（相信大部分人使用图床的目的也应该是使用markdown吧）
            python main.py -type insert --biantai 1 --value xx/autsKBEUobaujwT.png
                biantai参数的值为非0的时候value的传参应当是url的完整格式（如果直接获取url的话就应该是这样）
        """)

