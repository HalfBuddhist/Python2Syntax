#!/usr/bin/env python
# -*- coding:utf-8 -*-

class A(object):
    def __init__(self, num):
        self.prop_a = num

    def __getattr__(self, item):
        if item == 'hello':
            return 123

a = A(100)
print a.prop_a
print a.hello