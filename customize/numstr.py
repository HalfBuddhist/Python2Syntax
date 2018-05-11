#!/usr/bin/env python
# coding=utf-8
"""
a customize class.

python 未知bug, 在__str__函数里调用父类的函数，同时定义了__repr__ ＝ __str__函数，
调用str()内建函数就会出错，好是是一个无穷递归所造成的。

"""

class NumStr(object):
    def __init__(self, num=0, string=''):
        self.__num = num
        self.__string = string

    def __str__(self): # define for str()
        # return super(NumStr, self).__str__()
        return '[%d :: %r]' % (self.__num, self.__string)

    __repr__ = __str__

    def __add__(self, other): # define for s+o
        if isinstance(other, NumStr):
            return self.__class__(self.__num + other.__num, self.__string + other.__string)
        else:
            raise TypeError, 'Illegal argument type for built-in operation'

    def __mul__(self, num): # define for o*n
        if isinstance(num, int):
            return self.__class__(self.__num * num, self.__string * num)
        else:
            raise TypeError, 'Illegal argument type for built-in operation'

    def __nonzero__(self): # False if both are
        return self.__num or len(self.__string)

    def __norm_cval(self, cmpres):# normalize cmp()
        'conver the positive to 1 and the negative to -1, 0 to 0'
        return cmp(cmpres, 0)

    def __cmp__(self, other): # define for cmp()
        return self.__norm_cval(cmp(self.__num, other.__num)) + \
               self.__norm_cval(cmp(self.__string, other.__string))


if __name__ == '__main__':
    a = NumStr(1, 'hello')
    print a
    # print `a`