#!/usr/bin/env python
# coding=utf-8

from operator import add, mul
from functools import partial

add1 = partial(add, 1) # add1(x) == add(1, x)
mul100 = partial(mul, 100) # mul100(x) == mul(100, x)

print add1(10)
# 11
print add1(1)
# 2
print mul100(10)
#1000
print mul100(500)
#50000