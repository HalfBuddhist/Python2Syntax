#!/usr/bin/env python
# coding=utf-8
"""
例18.5 使用可调用的类 (mtsleep4.py)
此例中，我们传了一个可调用的类(的实例)，而不是仅传一个函数。相对mtsleep3.py 中的方
法来说，这样做更具面向对象的概念。
"""

import threading
from time import sleep, ctime

loops = [4,2]

class ThreadFunc(object):
    'the callable func'
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        # apply(self.func, self.args)
        self.func(*self.args)

def loop(nloop, nsec):
    print 'start loop', nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()

def main():
    print 'starting at:', ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops: # create all threads
        t = threading.Thread(target=ThreadFunc(loop, (i, loops[i]),loop.__name__))
        threads.append(t)

    for i in nloops: # start all threads
        threads[i].start()

    for i in nloops: # wait for completion
        print 'waiting ', i
        threads[i].join()
        print 'finished waiting ', i

    print 'all DONE at:', ctime()

if __name__ == '__main__':
    main()