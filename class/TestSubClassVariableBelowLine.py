#!/usr/bin/env python
# coding=utf-8
'''
测试下划线变量的继承性
'''

class P(object):
    __a__ = 1

    def __hello__(self):
        print "hello called"

    def __init__(self, pa = 100):
        self.__b__ = pa

class C(P):
    __a = 2
    def __hello(self):
        print self.__a

    def test(self):
        print C._P__a
    pass

if __name__ == '__main__':
    # print C.__a__
    # C().__hello__()
    # C()._P__hello()
    # C().test()
    print C.__a
    # print C()._P__b__