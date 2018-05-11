#!/usr/bin/env python
#coding=utf-8
'''
An example of reading and writing Unicode strings:Writes
a Unicode string to a file in utf-8 and reads itback in.
'''

#coding=utf-8

CODEC = 'utf-8'
FILE = 'unicode.txt'
hello_out = u"Hello world 你好！\n"
bytes_out = hello_out.encode(CODEC)
print type(hello_out)
print type(bytes_out)
f = open(FILE, "w")
f.write(bytes_out)
f.close()

f = open(FILE, "r")
bytes_in = f.read()
print(type(bytes_in))
f.close()
hello_in = bytes_in.decode(CODEC)
print(type(hello_in))
print hello_in