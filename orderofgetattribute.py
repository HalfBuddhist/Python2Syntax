#!/usr/bin/env python
# coding=utf-8
"""
验证 getattribute的顺序
"""

class DevNull2(object):
    def __get__(self, obj, typ=None):
        print 'Accessing attribute... ignoring'
    def __set__(self, obj, val):
        print 'Attempt to assign %r... ignoring' % (val)

class P(object):
    foo = [1,2,3]
    # foo = DevNull2()

ins = P()
print ins.foo
ins.foo = 'abc'
# ins.foo.append('abc')
print ins.foo
print ins.__getattribute__('foo')
del ins.foo
# P.foo = 222
print ins.foo
# del ins.foo
# print ins.foo