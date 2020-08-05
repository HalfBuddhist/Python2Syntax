#!/usr/bin/env python
# coding=utf-8
'''
测试下划线变量的继承性:
Conclusion:
    单下划线的为保护变量，可以继承；
    双下划线的为私有变量，不可以直接继承，只能通过_P_VarName的形式来访问；
    以下规则既适用于变量，也适用于成员函数；
'''

class P(object):
    __a__ = 1

    def __hello(self):
        print "hello called"

    def __init__(self, pa = 100):
        self.__b__ = pa
        self.__ts_pri = "hello"

class C(P):
    __a = 2
    def __hello(self):
        print self.__a

    def test(self):
        print C._P__a
    pass

if __name__ == '__main__':
    # print C.__a__
    # C()._C__hello()
    # C()._P__hello()
    # C().test()
    # print C.__a
    # print C()._P__b__


    # 测试对于私有变量的访问
    p = P()
    print p._P__ts_pri
