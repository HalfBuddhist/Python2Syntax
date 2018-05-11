#!/usr/bin/env python
# coding=utf-8
"""
元类示例
在第二个示例中，我们将创建一个元类，要求程序员在他们写的类中提供一个__str__()方法的
实现，这样用户就可以看到比我们在本章前面所见到的一般Python 对象字符串(<object object at
id>)更有用的信息。
如果您还没有在类中覆盖__repr__()方法，元类会(强烈)提示您这么做，但这只是个警告。如
果未实现__str__()方法，将引发一个TypeError 的异常，要求用户编写一个同名方法。以下是关于
元类的代码:

这个模块有一个元类和三个受此元类限定的类。每创建一个类，将打印一条输出语句。
"""

from warnings import warn

class ReqStrSugRepr(type):
    def __init__(cls, name, bases, attrd):
        super(ReqStrSugRepr, cls).__init__(name, bases, attrd)
        if '__str__' not in attrd:
            raise TypeError("Class requires overriding of __str__()")
        if '__repr__' not in attrd:
            warn('Class suggests overriding of __repr__()\n', stacklevel=3)

print '*** Defined ReqStrSugRepr (meta)class\n'

class Foo(object):
    __metaclass__ = ReqStrSugRepr
    def __str__(self):
        return 'Instance of class:', self.__class__.__name__
    def __repr__(self):
        return self.__class__.__name__

print '*** Defined Foo class\n'

class Bar(object):
    __metaclass__ = ReqStrSugRepr
    def __str__(self):
        return 'Instance of class:', self.__class__.__name__
print type(Bar)
print '*** Defined Bar class\n'
# print Bar.__mro__

class FooBar(object):
    __metaclass__ = ReqStrSugRepr

print '*** Defined FooBar class\n'