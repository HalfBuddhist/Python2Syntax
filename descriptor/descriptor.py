#!/usr/bin/env python
# coding=utf-8
"""
测试描述符
"""

class General(object):
    def __init__(self):
        self.a = 123

class DevNull1(object):
    def __get__(self, obj, typ=None):
        pass
    def __set__(self, obj, val):
        pass

class DevNull2(object):
    def __get__(self, obj, typ=None):
        print 'Accessing attribute... ignoring'
    def __set__(self, obj, val):
        print 'Attempt to assign %r... ignoring' % (val)

class DevNull3(object):
    def __init__(self, name=None):
        self.name = name
    def __get__(self, obj, typ=None):
        print 'Accessing [%s]... ignoring' % (self.name)
    def __set__(self, obj, val):
        print 'Assigning %r to [%s]... ignoring' % (val, self.name),


class C1(object):
    # foo = DevNull1()
    foo = DevNull3('foo')

c3 = C1()
c3.foo = 'bar'
print 'c1.foo contains:', c3.foo
# c1.foo contains: None

# dev null 3
print 'Let us try to sneak it into c3 instance...'
print c3.__dict__
c3.__dict__['foo'] = 'bar'
print c3.__dict__
x = c3.foo
print 'c3.foo contains:', x
# c3.foo contains: None
print "c3.__dict__['foo'] contains: %r" % (c3.__dict__['foo'])

class C2(object):
    foo = General()
    def __init__(self):
        self.a = 'a'
    # foo = DevNull3('foo')

c3 = C2()
print c3.__dict__
c3.foo = 'bar'
print 'c11111.foo contains:', c3.foo
# c1.foo contains: None