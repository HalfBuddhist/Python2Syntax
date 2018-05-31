#!/usr/bin/env python
# coding=utf-8

import logging
import logging.handlers
import sys


# 实例化handler
handler = logging.StreamHandler(stream=sys.stdout)

fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'

formatter = logging.Formatter(fmt)   # 实例化formatter
handler.setFormatter(formatter)      # 为handler添加formatter

logger = logging.getLogger('tst')    # 获取名为tst的logger
logger.addHandler(handler)           # 为logger添加handler
logger.setLevel(logging.INFO)

logger.info('first info message')
logger.debug('first debug message')

# logging.info('testsdfdf')