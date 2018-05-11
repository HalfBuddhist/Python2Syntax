#!/usr/bin/env python
# coding=utf-8
"""
test mysql operation
"""

import MySQLdb

cxn = MySQLdb.connect(user='root')
# cxn.query('DROP DATABASE testpython')
# File "<stdin>", line 1, in ?
# _mysql_exceptions.OperationalError: (1008, "Can't drop database 'test'; database
# doesn't exist")
cxn.query('CREATE DATABASE testpython')

cxn.query("GRANT ALL ON test.* to ''@'localhost'")
cxn.commit()
cxn.close()