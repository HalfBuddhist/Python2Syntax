#!/usr/bin/env python
# coding=utf-8
'''
测试实例对于类属性的访问
'''

class A(object):
    a = 123
    def __init__(self):
        pass

a1 = A()
print a1.__dict__
a1.a = 2344
print a1.__dict__
print a1.a
a2 = A()
print a2.a
print a2.__dict__
print a2.__class__.__dict__