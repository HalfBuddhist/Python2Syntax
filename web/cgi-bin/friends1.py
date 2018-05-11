#!/usr/bin/env python
# coding=utf-8
"""
Example 20.4 Results Screen CGI code (friends1.py)
CGI 脚本在表单上抓取person 和howmany 字段，并用这些数据生成动态的结果示图。
"""

import cgi

reshtml = '''Content-Type: text/html\n
<HTML><HEAD><TITLE>
Friends CGI Demo (dynamic screen)
</TITLE></HEAD>
<BODY><H3>Friends list for: <I>%s</I></H3>
Your name is: <B>%s</B><P>
You have <B>%s</B> friends.
</BODY></HTML>'''

form = cgi.FieldStorage()
who = form['person'].value
howmany = form['howmany'].value
print reshtml % (who, who, howmany)