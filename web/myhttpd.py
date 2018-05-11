#!/usr/bin/env python
# coding=utf-8
"""
Example 20.9 Simple Web Server (myhttpd.py)
这个简单的Web 服务器可以读取GET 请求，获取Web 页面（.html 文件）并将其返回给客户端。
它通过使用BaseHTTPServer 的BaseHTTPRequestHandler 处理器执行do_GET()方法来处理GET 请求。
"""

from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            f = open(curdir + sep + self.path)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

def main():
    try:
        server = HTTPServer(('', 8001), MyHandler)
        print 'Welcome to the machine...',
        print 'Press ^C once or twice to quit.'
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()