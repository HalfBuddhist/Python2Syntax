#!/usr/bin/env python
# coding=utf-8

import time, sched

#被调度触发的函数
def event_func(msg):
    print "Current Time:",time.time(),'msg:',msg

if __name__ == "__main__":
    #初始化sched模块的scheduler类
    event_func('stat time')
    s = sched.scheduler(time.time,time.sleep)
    #设置两个调度
    # s.enter(2,2,event_func,("Small event.",))
    # s.enter(5,1,event_func,("Big event.",))
    # print 'c'
    # s.run()
    # print 'a'
    # s.enter(5,1,event_func,("another event.",))
    # s.run()
    # while True:
    #     print 'b'
    #     time.sleep(100)
