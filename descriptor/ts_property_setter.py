#!/usr/bin/env python
# coding=utf-8
"""
关于setter of the property builtin function 的例子
property(fget=None, fset=None, fdel=None, doc=None)
"""

class HideX(object):
    def __init__(self, x):
        self.x = x

    def __get_x(self):
        return ~self.__x

    def __set_x(self, x):
        assert isinstance(x, int), '"x" must be an integer!'
        self.__x = ~x

    x = property(__get_x, __set_x)

############### test intit ###############
inst = HideX(20)
print inst.x
# 20
############### test set ###############
inst.x = 30
print inst.x
# 30

############### 没有强制使用property()，因为它允许对属性方法的访问(由于在类定义中包含属性方法): ###############
inst._HideX__set_x(40) # can we require inst.x = 40?
print inst.x
# 40