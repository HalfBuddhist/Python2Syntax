#!/usr/bin/env python
# coding: UTF-8
"""
unittest to test the mydict classs.
"""

import unittest

from mydict import Dict


class TestDict(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print "setUpClass...."

    @classmethod
    def tearDownClass(cls):
        print "tearDownClass...."

    def setUp(self):
        print "setUP...."

    def tearDown(self):
        print "tearDown..."

    @unittest.skip("skip for now")
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEquals(d.a, 1)
        self.assertEquals(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEquals(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEquals(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty


if __name__ == '__main__':
    unittest.main(verbosity=2)
