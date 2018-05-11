#!/usr/bin/env python
# coding=utf-8

import sys

print 'you entered', len(sys.argv), 'arguments...'
print 'they were:', str(sys.argv)

# for verify use or not
# if len(sys.argv) > 1:
#     if sys.argv[1] == 'verify':
#         logger.info('Merging statistic data for verify.')
#         startIndex = 3
#         fileNameAppend = 'verify'
#     else:
#         startIndex = 2
#         fileNameAppend = ''