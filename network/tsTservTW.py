#!/usr/bin/env python
# coding=utf-8
"""
例16.7 Twisted Reactor 时间戳TCP 服务器(tsTservTW.py)
这是一个使用Twisted Internet 类的时间戳TCP 服务器
"""

from twisted.internet import protocol, reactor
from time import ctime

PORT = 21567

class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print '...connected from:', clnt
    def dataReceived(self, data):
        self.transport.write('[%s] %s' % (ctime(), data))

factory = protocol.Factory()
factory.protocol = TSServProtocol
print 'waiting for connection...'
reactor.listenTCP(PORT, factory)
reactor.run()