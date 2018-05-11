#!/usr/bin/env python
# coding=utf-8
"""
test mysql official connector
"""

import mysql.connector as mysql

cxn = mysql.connect(user='root', passwd='252019', db='Lottery',use_unicode=True, charset='utf8')
# cxn = MySQLdb.connect(user='root')
# cxn.query('DROP DATABASE testpython')
# File "<stdin>", line 1, in ?
# _mysql_exceptions.OperationalError: (1008, "Can't drop database 'test'; database
# doesn't exist")
cursor = cxn.cursor()
cursor.execute('CREATE DATABASE testpython')

cursor.execute("GRANT ALL ON test.* to ''@'localhost'")
cxn.commit()
cursor.close()
cxn.close()
