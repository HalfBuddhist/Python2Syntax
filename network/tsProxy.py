#!/usr/bin/env python
# coding=utf-8

import urllib2
import urllib
import re

url = 'http://www.ip138.com/'
url1 = 'http://1111.ip138.com/ic.asp'


def testProxies():
    'urllib.urlopen(proxies={}) method, works for http and socks'
    response = urllib.urlopen(url,proxies={'socks':'socks://127.0.0.1:7070'})
    content = response.read().decode('GB18030')
    response.close()
    print(content)
    open('138.html','w').write(content.encode('utf8'))


def testSetProxy():
    'the urllib2.request.set_proxy method, for now does not work for socks proxy, \
    works for the http proxies'
    request = urllib2.Request(url1)
    # request.add_header('Range', 'bytes=%d-%d' %self.headerrange)
    # request.set_proxy('socks://127.0.0.1:7070','socks')
    request.set_proxy('123.121.104.166:8118','http')
    response = urllib2.urlopen(request)
    content = response.read().decode('GB18030')
    response.close()
    print content
    open('138.html','w').write(content.encode('GB18030'))

def tsProxyHandler():
    'http works, socks not.'
    # handlers = [urllib2.ProxyHandler({'http': 'http://%s/' % '123.121.104.166:8118'})]
    handlers = [urllib2.ProxyHandler({'socks': 'socks://%s/' % '127.0.0.1:7070'})]
    opener = urllib2.build_opener(*handlers)
    # response = opener.open(urllib2.quote(url1, safe=":/"), timeout=30)
    response = opener.open(url1, timeout=30)
    content = response.read().decode('GB18030')
    response.close()
    print content
    open('138.html','w').write(content.encode('GB18030'))


# proxy_handler = urllib2.ProxyHandler({"socks" : 'socks://127.0.0.1:3128'})
# opener = urllib2.build_opener(proxy_handler)
# urllib2.install_opener(opener)




# enable_proxy = True
# proxy_handler = urllib2.ProxyHandler({"http" : 'your_proxy'})
# null_proxy_handler = urllib2.ProxyHandler({})
# if enable_proxy:
#     opener = urllib2.build_opener(proxy_handler)
# else:
#     opener = urllib2.build_opener(null_proxy_handler)
# urllib2.install_opener(opener)

def testProxy(ip, port, type):
    url = 'http://1111.ip138.com/ic.asp'
    response = urllib.urlopen(url, proxies={type: type+'://'+ip+':'+port})
    content = response.read().decode('GB18030')
    code = response.getcode()
    response.close()
    print(code)
    # print(content)[123.121.104.166] 来自：北京市 联通
    # open('138.html','w').write(content.encode('utf8'))
    # result_pattern = re.search(ur'您的IP是：(.*)</center>', content)
    result_pattern = re.search(ur'您的IP是：\[(.*)\] 来自：(.*)</center>', content)
    result_ip = result_location = None
    if result_pattern is not None:
        result_ip = result_pattern.group(1)
        result_location = result_pattern.group(2)
    print result_ip, result_location
    if result_ip == ip:
        print 'proxy works. :)'
    else:
        print('proxy is not annonimous.')


if __name__ == '__main__':
    # testProxy('123.121.104.166','8118', 'http')
    testSetProxy()
    # tsProxyHandler()
    pass