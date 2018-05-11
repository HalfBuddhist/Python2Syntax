#!/usr/bin/env python
# coding=utf-8
"""
python中的循环校验码，后面添加了右移操作
"""

import urlparse
import binascii


def right_shift(val, n):
    """
    无符号右移
    """
    return val >> n if val >= 0 else (val + 0x100000000) >> n


url = "http://ib.365yg.com/video/urls/v/1/toutiao/mp4/a519dca5dd6442839c23a73889e56395"
# url = 'http://i.snssdk.com/video/urls/v/1/toutiao/mp4/%s' % vid
n = urlparse.urlparse(url).path + '?r=' + "08633517709597993"
c = binascii.crc32(n)
s = right_shift(c, 0)

print s
