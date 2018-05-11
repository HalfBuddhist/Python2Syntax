#!/usr/bin/env python
# coding=utf-8
"""
测试propery builtin function
在类中建立一个只读的整数属性，用逐位异或操作符将它隐藏起来：
"""

class ProtectAndHideX(object):
    def __init__(self, x):
        assert isinstance(x, int), '"x" must be an integer!'
        self.__x = ~x

    def get_x(self):
        return ~self.__x

    x = property(get_x)


############### test assert ###############
# inst = ProtectAndHideX('foo')
# result of output
# Traceback (most recent call last):
# File "<stdin>", line 1, in ?
# File "prop.py", line 5, in __init__
# assert isinstance(x, int), \
# AssertionError: "x" must be an integer!

############### test set the new value ###############
inst = ProtectAndHideX(10)
print 'inst.x =', inst.x
# inst.x = 10
inst.x = 20
# Traceback (most recent call last):
# File "<stdin>", line 1, in ?
# AttributeError: can't set attribute