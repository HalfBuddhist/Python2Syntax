# 如何让Timer循环呢，一种很山寨的方法是……在test_func中再次调用Timer…start…

import threading
import time

def timer_start():
    t = threading.Timer(5,test_func,("msg1","msg2"))
    t.start()

def test_func(msg1,msg2):
    print "I'm test_func,",msg1,msg2
    timer_start()

if __name__ == "__main__":
    timer_start()
    while True:
        time.sleep(1)