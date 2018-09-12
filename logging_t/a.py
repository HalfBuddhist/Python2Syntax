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
import logging.config
# import c

from b import output
logging.config.fileConfig("logging.conf")   # 采用配置文件

# create logger
logger = logging.getLogger("simpleExample")

# "application" code
logger.debug("debug message")
logger.info("info message")
logger.warn("warn message")
logger.error("error message")
logger.critical("critical message")

output()