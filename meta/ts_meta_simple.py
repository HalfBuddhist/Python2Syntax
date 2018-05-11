#!/usr/bin/env python
# coding=utf-8
"""
元类简单示例
我们第一个关于元类的示例非常简单(希望如此)。它只是在用元类创建一个类时，显示时间标
签。(你现在该知道，这发生在类被创建的时候。)
"""

from time import ctime

print '*** Welcome to Metaclasses!'
print '\tMetaclass declaration first.'

class MetaC(type):
    def __init__(cls, name, bases, attrd):
        super(MetaC, cls).__init__(name, bases, attrd)
        print '*** Created class %r at: %s' % (name, ctime())

print '\tClass "Foo" declaration next.'

class Foo(object):
    __metaclass__ = MetaC
    def __init__(self):
        print '*** Instantiated class %r at: %s' % (self.__class__.__name__, ctime())

print '\tClass "Foo" instantiation next.'
f = Foo()
print '\tDONE'