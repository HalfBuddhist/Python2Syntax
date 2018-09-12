#!/usr/bin/env python
# coding=utf-8
# 
# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2018/9/3
"""
"""

import logging

logger = logging.getLogger("b")

s = "b"

def output():
    logger.info("info log from {}.".format(s))
    logger.debug("debug log from {}.".format(s))
    logger.warning("warning log from {}.".format(s))
    logger.error("error log from {}.".format(s))

if __name__ == "__main__":
    output()