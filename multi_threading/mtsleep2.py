#!/usr/bin/env python
# coding=utf-8
"""
例18.3 使用线程和锁 (mtsleep2.py)
这里，使用锁比mtsleep1.py 那里在主线程中使用sleep()函数更合理。
"""

import thread
from time import sleep, ctime

loops = [4,2]

def loop(nloop, nsec, lock):
    '''
    :argument nloop the loop id
    :argument nsec the loop time
    :argument lock the lock object
    '''
    print 'start loop', nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()
    lock.release()

def main():
    print 'starting at:', ctime()
    locks = []
    nloops = range(len(loops))

    for i in nloops:
        lock = thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in nloops:
        thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in nloops:
        while locks[i].locked():
            # print 'cheking' # 竟然没用阻塞，而用了死循环来检查锁的状态，够狠！
            pass

    print 'all DONE at:', ctime()

if __name__ == '__main__':
    main()