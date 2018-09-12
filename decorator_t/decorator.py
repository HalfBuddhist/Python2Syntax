#!/usr/bin/env python
# coding=utf-8
'测试被修饰的函数带参数的情况 - 参数也是可以改变的，要看如何被包裹'

from time import ctime, sleep

def tsfunc(func):
    def wrappedFunc(var):
        print '[%s] %s() called' % (ctime(), func.__name__)
        return func(var)
    return wrappedFunc

@tsfunc
def foo(var):
    print(var)
    pass

foo('hello')
sleep(4)
for i in range(2):
    sleep(1)
    foo('hello')
