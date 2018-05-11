#!/usr/bin/env python
# coding=utf-8

import json
 
obj = [[1,2,3],123,123.123,'abc',{'key1':(1,2,3),'key2':(4,5,6)}]
encodedjson = json.dumps(obj)
print repr(obj)
# print str(obj)
# print `obj`
print encodedjson