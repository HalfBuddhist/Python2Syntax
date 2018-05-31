#!/usr/bin/env python
# coding=utf-8

import threading
import time

def test_func(msg1,msg2):
    print "I'm test_func,",msg1,msg2

if __name__ == "__main__":
    t = threading.Timer(5,test_func,("msg1","msg2"))
    print 'a'
    t.start()
    print 'c'
    # while True:
    #     print 'b'
    #     time.sleep(3)
