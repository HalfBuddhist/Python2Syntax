#coding=utf-8

import re

#  查找通常被用来表示空白字符的反斜线-字符对(backslash-character pairs)。
#m = re.search('\\[rtfvn]', r'Hello World!\n')
m = re.search(r'\\[rtfvn]', r'Hello World!\n')

if m is not None:
    print m.group()

