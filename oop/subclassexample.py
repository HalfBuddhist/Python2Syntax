#!/usr/bin/env python
# coding=utf-8
'''
对于内建可变类型的继承
'''

class SortedKeyDict(dict):
    def keys(self):
        return sorted(super( SortedKeyDict, self).keys())

d = SortedKeyDict((('zheng-cai', 67), ('hui-jun', 68),('xin-yi', 2)))


if __name__ == '__main__':
    print 'By iterator:'.ljust(12), [key for key in d]
    print 'By keys():'.ljust(12), d.keys()