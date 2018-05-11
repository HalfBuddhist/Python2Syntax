#!/usr/bin/env python
# coding=utf-8

import base64
import urllib2

# method 1

main_url = "aHR0cDovL3YxLXR0Lml4aWd1YS5jb20vNzkxNTU0YWNlOGQ5Y2I3Yzg5ZDE5YjM3ZjJjZjZjNTQvNWFkMzA4NDIvdmlkZW8vbS8yMjBhNGNhNmEzNDFjMjQ0YmU1OTc4MjBlNzYwNzUyMDFhNjExNTYwMjEzMDAwMDhjYTNiNjdjMzgyYi8="
# main_url = "aHR0cDovL3YzYi5wc3RhdHAuY29tLzI2MDg1ZDZjMjBkY2ZjY2FmYmU1NThlYjRmYmMxNGZjLzVhZDMwNzNjL3ZpZGVvL20vMjIwYTRjYTZhMzQxYzI0NGJlNTk3ODIwZTc2MDc1MjAxYTYxMTU2MDIxMzAwMDA4Y2EzYjY3YzM4MmIv"
print base64.standard_b64decode(main_url)
# output: http://v3a.pstatp.com/a1ec1fc39496a8c852c2e8fc4c74fe13/5ad2d697/video/m/220a4ca6a341c244be597820e76075201a61156021300008ca3b67c382b/



# method 2
from base64 import encodestring

# b64str = encodestring('%s:%s' % (LOGIN, PASSWD))[:-1]