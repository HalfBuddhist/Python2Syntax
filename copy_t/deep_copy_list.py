#!/usr/bin/env python
# coding=utf-8
"""
the deepcopy copy everthing recursively.
"""

import copy


class a(object):
    def __init__(self):
        self.num = 1


b = [a() for _ in xrange(5)]
for e in b:
    print id(e)
c = copy.deepcopy(b)
print "#" * 100
for e in c:
    print id(e)
