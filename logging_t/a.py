#!/usr/bin/env python
# coding=utf-8
#
# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2018/9/3
"""测试日志导入时的config问题：
结论：还是得在所有的本地顶级代码执行前，进行配置。
以前的main函数里配置的方法，在import另外的模块时，生成的logger的配置信息会出错。
"""

import logging
import logging.config
import c

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