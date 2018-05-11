#!/usr/bin/env python
# coding=utf-8
"传递和调用(内建）函数"

def convert(func, seq):
    'conv. sequence of numbers to same type'
    return [func(eachNum) for eachNum in seq]

myseq = (123, 45.67, -6.2e8, 999999999L)
print 'int'
print convert(int, myseq)
print 'long'
print convert(long, myseq)
print 'float'
print convert(float, myseq)