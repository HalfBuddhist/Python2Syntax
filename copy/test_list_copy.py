#!/usr/bin/env python
# coding=utf-8
"""
the sorted funtion is a shallow copy.
"""


class a(object):
    def __init__(self):
        self.num = 1


b = [a() for _ in xrange(6)]
for i in b:
    print id(i)

# b.sort(reverse=True)
print "*" * 100
# for i in b:
# print id(i)

c = sorted(b)
for i in c:
    i.isUsed = False
    print id(i), i.isUsed