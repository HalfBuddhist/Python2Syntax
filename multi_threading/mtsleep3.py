#!/usr/bin/env python
# coding=utf-8
"""
例18.4 使用threading 模块 (mtsleep3.py)
threading 模块的Thread 类有一个join()函数，允许主线程等待线程的结束。
"""

import threading
from time import sleep, ctime

loops = [4,2]

def loop(nloop, nsec):
    print 'start loop', nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()

def main():
    print 'starting at:', ctime()
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for i in nloops: # start threads
        threads[i].start()

    for i in nloops: # wait for all
        print 'waiting ', i
        threads[i].join() # threads to finish
        print 'finished waiting ', i

    print 'all DONE at:', ctime()

if __name__ == '__main__':
    main()