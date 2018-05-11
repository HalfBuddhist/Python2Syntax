#!/usr/bin/env python
# coding=utf-8
"""从asc2文件中解析load json对象，默认是以unicode-utf8编码的方式"""

import json
from json import decoder, scanner

from json.scanner import make_scanner
from _json import scanstring as c_scanstring

_CONSTANTS = json.decoder._CONSTANTS

py_make_scanner = scanner.py_make_scanner

# Convert from unicode to str
def str_scanstring(*args, **kwargs):
    result = c_scanstring(*args, **kwargs)
    return str(result[0]), result[1]

# Little dirty trick here
json.decoder.scanstring = str_scanstring

class StrJSONDecoder(decoder.JSONDecoder):
    def __init__(self, encoding=None, object_hook=None, parse_float=None,
            parse_int=None, parse_constant=None, strict=True,
            object_pairs_hook=None):
        self.encoding = encoding
        self.object_hook = object_hook
        self.object_pairs_hook = object_pairs_hook
        self.parse_float = parse_float or float
        self.parse_int = parse_int or int
        self.parse_constant = parse_constant or _CONSTANTS.__getitem__
        self.strict = strict
        self.parse_object = decoder.JSONObject
        self.parse_array = decoder.JSONArray
        self.parse_string = str_scanstring
        self.scan_once = py_make_scanner(self)

# And another little dirty trick there
_default_decoder = StrJSONDecoder(encoding=None, object_hook=None,
                               object_pairs_hook=None)

json._default_decoder = _default_decoder

j = {1:'2', 1.1:[1,2,3], u'test': {12:12, 13:'o'}}
print json.loads(json.dumps(j))