#!/usr/bin/env python
# coding=utf-8
"""
test sqlite operation
"""

import sqlite3

cxn = sqlite3.connect('test')
cur = cxn.cursor()
# cur.execute('CREATE TABLE users(login VARCHAR(8), uid INTEGER)')
# cur.execute('INSERT INTO users VALUES("john", 100)')
# cur.execute('INSERT INTO users VALUES("jane", 110)')
cur.execute('SELECT * FROM users')

for eachUser in cur.fetchall():
 print eachUser
# (u'john', 100)
# (u'jane', 110)
# cur.execute('DROP TABLE users')
# <sqlite3.Cursor object at 0x3d4320>
cur.close()
cxn.commit()
cxn.close()