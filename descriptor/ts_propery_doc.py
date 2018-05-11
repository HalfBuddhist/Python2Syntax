#!/usr/bin/env python
# coding=utf-8
"""
描述符示例，
给属性添加一个文档字符串
"""

from math import pi


def get_pi(dummy):
    return pi
    # pass
class PI(object):
    pi = property(get_pi, doc='Constant "pi"')

############### test get ###############
inst = PI()
print inst.pi
# 3.1415926535897931

############### test get ###############
print PI.pi.__doc__
# Constant "pi"

