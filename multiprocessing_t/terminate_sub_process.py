#!/usr/bin/env python
# coding=utf-8
# 
# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2018/9/7
"""Terminate the sub process.
method 1: sub_process.terminate.
method 2: os.kill(pid, sig_kill/sig_term)
method 3: sig.alarm to nofify the sub procees to exit
          (raise exception or call the exit() method).
"""

import multiprocessing
import signal
import sys
from time import sleep

timeout = 10  # seconds
check_interval = 1 # seconds


def raise_timeout(signum, frame):
    raise Exception("train timeout.")

def raise_timeout2(signum, frame):
    raise Exception("train timeout2.")
# def

def func(conn):
    try:
        signal.signal(signal.SIGALRM, raise_timeout)
        # signal.signal(signal.SIGALRM, raise_timeout2)
        # signal.signal(signal.SIGTERM, signal.SIG_IGN)
        # sleep(10)
        # sys.exit()
        signal.alarm(1)
        # sleep(6)
        a = 1
        while True:
            a += 1
            a %= 100
    except Exception as e:
        print("Catch the exception.")

parent_conn, child_conn = multiprocessing.Pipe()
sub_process = multiprocessing.Process(target=func, args=(child_conn,))
sub_process.start()
print(sub_process.pid)
child_conn.close()

# try:
#     elapsed_time = 0
#     while timeout is None or elapsed_time < timeout:
#         if timeout:
#             elapsed_time += check_interval
#             poll_status = parent_conn.poll(check_interval)
#         else:
#             poll_status = parent_conn.poll(None)
#
#         if poll_status:
#             ret_val = parent_conn.recv()
#             # occur error, raise the exception.
#             if isinstance(ret_val, RuntimeWatchException):
#                 raise ret_val
#             # return ret_val
#     # timeout
#     # print("Come to kill {}.".format(func.__name__))
#     # sub_process.terminate()
#     # print("func |%s| call timeout." % func.__name__)
#     # raise TimeoutException("func |%s| call timeout." % func.__name__)
# finally:
#     sub_process.join()
print("Waiting the sub pro.")
sub_process.join()
# try:
#     sub_process.join()
# except Exception as e:
#     print("Catch the exception.")

print("Main pro exit.")
