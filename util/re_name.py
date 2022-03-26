"""
@Project ：Spider for imagebed-sm.ms 
@File    ：re_name.py
@Date    ：2022/3/26 14:02 
"""
# -*- coding: UTF-8 -*-
import re

def re__(word, re_rule=None):
    if re_rule is None:
        return None
    else:
        rule = re.compile(re_rule)
        data = re.findall(rule, word)
        print(data)
        return data