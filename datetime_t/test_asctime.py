#!/usr/bin/env python
# coding=utf-8
'''
你可以根据需求选取各种格式，但是最简单的获取可读的时间模式的函数是asctime():
'''

import datetime
import time  # 引入time模块

ticks = time.time()
print "当前时间戳为:", ticks

localtime = time.asctime(time.localtime(time.time()))
print "本地时间为 :", localtime

