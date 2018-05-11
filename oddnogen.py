#!/usr/bin/env python
# coding=utf-8

from random import randint as ri

def odd(n):
    return n % 2

allNums = []
# for eachNum in range(9):
#     allNums.append(randint(1, 99))
# print allNums
# print filter(odd, allNums)
# print(filter(lambda x : x % 2, allNums))
# print [x for x in allNums if  x%2]
print [n for n in [ri(1,99) for i in range(9)] if n%2]