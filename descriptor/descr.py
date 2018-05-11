#!/usr/bin/env python
# coding=utf-8
"""
描述符示例，它尝试用文件系统保存一个属性的内容，这是个雏形版本。
这个类是一个雏形，但它展示了描述符的一个有趣的应用－－可以在一个文件系统上保存属性
的内容。

描述符是用来控制地于实例属性的访问，并非是控制对于类属性的访问。
"""

import os
import pickle

class FileDescr(object):
    saved = []

    def __init__(self, name=None):
        self.name = name

    def __get__(self, obj, typ=None):
        if self.name not in FileDescr.saved:
            raise AttributeError, "%r used before assignment" % self.name
        try:
            f = open(self.name, 'r')
            val = pickle.load(f)
            f.close()
            return val
        except(pickle.InpicklingError, IOError,EOFError, AttributeError, ImportError, IndexError), e:
            raise AttributeError, "could not read %r: %s" % self.name

    def __set__(self, obj, val):
        f = open(self.name, 'w')
        try:
            try:
                pickle.dump(val, f)
                FileDescr.saved.append(self.name)
            except (TypeError, pickle.PicklingError), e:
                raise AttributeError, "could not pickle %r" % self.name
        finally:
            f.close()

    def __delete__(self, obj):
        try:
            os.unlink(self.name)
            FileDescr.saved.remove(self.name)
        except (OSError, ValueError), e:
            pass


class MyFileVarClass(object):
    foo = FileDescr('foo')
    bar = FileDescr('bar')

############### test access form the class ###############
# MyFileVarClass.foo = 123
# print MyFileVarClass.foo
fvc = MyFileVarClass()
print fvc
# print fvc.foo
fvc.foo = 456
print fvc.foo
# print MyFileVarClass.foo

############### test the __get__method ###############
# fvc = MyFileVarClass()
# print fvc.foo
# Traceback (most recent call last): File "<stdin>", line 1, in ?
# File "descr.py", line 14, in __get__
# raise AttributeError, \
# AttributeError: 'foo' used before assignment

############### test the __set__method ###############
# fvc.foo = 42
# fvc.bar = 'leanna'
# print fvc.foo, fvc.bar
# 42 leanna

############### test the __delete__method ###############
# del fvc.foo
# print fvc.foo, fvc.bar
# Traceback (most recent call last): File "<stdin>", line 1, in ?
# File "descr.py", line 14, in __get__
# raise AttributeError, \
# AttributeError: 'foo' used before assignment

############### test the __delete__method ###############
# fvc.foo = __builtins__
# Traceback (most recent call last):
# File "<stdin>", line 1, in ?
# File "descr.py", line 35, in __set__
# raise AttributeError, \ AttributeError: could not pickle 'foo'