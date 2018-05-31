#!/usr/bin/env python
# coding=utf-8
'''
test the date and time, 
test the timedelta function.
'''

#  获取日期：
import datetime    #调用事件模块
today =datetime.date.today()    #获取今天日期
deltadays = datetime.timedelta(days=1)    #确定日期差额，如前天 days=2
yesterday = today - deltadays    # 获取差额日期，昨天
tomorrow = today + deltadays     # 获取差额日期，明天
# 格式化输出
ISOFORMAT='%Y-%m-%d' #设置输出格式
print today.strftime(ISOFORMAT)
print yesterday.strftime(ISOFORMAT)
print (tomorrow - datetime.timedelta(days=20)).strftime(ISOFORMAT)