#!/usr/bin/env python
# coding=utf-8
# 
# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2018/11/22
"""获得时区信息
"""

## method 1：但是获得的好像是 UTC 时区，（ mac 与 linux 不同 ）
# import time
# print(time.strftime("%z", time.gmtime()))

## method 2: 获得的为空。
# import datetime
# print(datetime.datetime.now().strftime("%Z"))

## method3: 可行。
import time
str = time.strftime('%z', time.localtime())
print(str)
