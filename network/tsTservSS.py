#!/usr/bin/env python
# coding=utf-8
"""
例16.5 SocketServer 时间戳服务器(tsTservSS.py)
使用SocketServer 里的TCPServer 和StreamRequestHandler 类创建一个时间戳TCP服务器。
"""

from SocketServer import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
    def handle(self):
        print '...connected from:', self.client_address
        self.wfile.write('[%s] %s' % (ctime(), self.rfile.readline()))

try:
    tcpServ = TCP(ADDR, MyRequestHandler)
    print 'waiting for connection...'
    tcpServ.serve_forever()
except (EOFError, KeyboardInterrupt), e:
    tcpServ.server_close()
    raise e