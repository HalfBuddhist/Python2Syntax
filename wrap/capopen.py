#!/usr/bin/env python
# coding=utf-8
"""
只准写入大写字母到文件的包装类
"""

import __builtin__

class open(object):
    def __init__(self, fn, mode='r', buf=-1):
        self.file = __builtin__.open(fn, mode, buf)

    def __str__(self):
        return str(self.file)

    def __repr__(self):
        return `self.file`

    def write(self, line):
        self.file.write(line.upper())

    def __getattr__(self, attr):
        return getattr(self.file, attr)

f = open('capopen.txt', 'w')
f.write('helo ')
f.write('world\n')
f.write('lqw write at night.\n')
f.close()
print f
