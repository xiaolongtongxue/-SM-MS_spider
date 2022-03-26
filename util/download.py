"""
@Project ：Spider for imagebed-sm.ms 
@File    ：download.py
@Date    ：2022/3/26 14:09 
"""
# -*- coding: UTF-8 -*-
import requests

def download_(pos: str, url: str):
    print("准备下载到：" + pos)
    r = requests.get(url)
    try:
        with open(pos, "wb") as f:
            try:
                f.write(r.content)
                print("已完成项目：" + url)
                print("下载地址：" + pos)
            except Exception as e:
                print("Download error")
                print(e)
    except FileNotFoundError:
        print("*"*50)
        print("FileNot found")
        print("*"*50)
