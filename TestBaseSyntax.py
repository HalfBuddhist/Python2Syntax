import socket
import math
import os
import sys

__author__ = 'Qingwei'

print __author__

baiduip = socket.gethostbyname('baidu.com')

print(baiduip)

x = math.sin(math.pi/6)

print(x)

curdir = os.getcwd()

print(curdir)

def test_func():
    "hello there"
    print('hello world!')
    print('test func')

def test_parameter(p1, p2):
    print(p1)
    print p2


def my_sum(p1, p2):
    return p1 + p2

def my_cal(p1, p2):
    return p1 + p2, p1 - p2, p1 * p2, p1 / p2

def test_pre(x, y, z = 12):
    print 'test xyz'
    print x, y, z



print('entray')

test_func()

test_parameter(2, 3)

print '1+2=', my_sum(1,2)

print my_cal(1, 2)


test_pre(2, 1)

# test_pre(z=1,1,2)

print('end')


l1 = [1,2,3,4]

scubes = map(lambda(x):x**3, l1)

print(scubes)

abc = [x**3 for x in l1]

print(abc)

l2 = [0,1,2,3,16]
l2[3:4] = [14,8]

print(l2)

print l2.sort()

print(l2)

if 1 < 2: print ' 1 < 2'
if 1<3:
    print l2

fn = ['ian', 'stuart', 'david']
ln = ['bairnson', 'elliott', 'paton']

for i, j in zip(fn, ln):
    print ('%s %s' % (i,j)).title()


# sys.exit() #exit the current python environment.


aList = ['tao', 93, 99, 'time']
aTuple = tuple(aList)
print aList, aTuple
(['tao', 93, 99, 'time'], ('tao', 93, 99, 'time'))
print aList == aTuple
anotherList = list(aTuple)
print aList == anotherList  # compare the elements in the list and tuple
print aList is anotherList

print id(aList)
print [id(x) for x in aList]
print id(aTuple)
print [id(x) for x in aTuple]
print(id(anotherList))
print [id(x) for x in anotherList]

print "-" * 30

print [id(x) for x in aList, aTuple, anotherList]

# the generator
print "-" * 30

def cols(): # example of simple generator
    yield 56
    yield 2
    yield 1
a = cols()
print max(a)
print "-" * 30
a = cols()
print min(a) #only onceba

print "-" * 30

def testArg(*test):
    print 'test Arg'
    print(test)

testArg('ss')

# x = 1
# a = lambda : x+1
# print a(x)

print "+" * 30

x = 10
def foo():
    y = 5
    bar = lambda :x+y
    print bar
    y = 8
    print bar

foo()

print "+" * 30

f = open('cardlog.txt')
f.close()

print `f`
