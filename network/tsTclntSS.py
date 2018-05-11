#!/usr/bin/env python
# coding=utf-8
"""
例16.6 SocketServer 时间戳TCP 客户端(tsTclntSS.py)
这是一个时间戳TCP 客户端，它知道如何与SocketServer 里StreamRequestHandler 对象进行
通讯。
"""

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = raw_input('> ')
    if not data:
        break
    tcpCliSock.send('%s\r\n' % data)
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print data.strip()
    tcpCliSock.close()