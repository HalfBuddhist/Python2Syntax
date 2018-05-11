#!/usr/bin/env python
# coding=utf-8
"""
list remove according to the __eq__ funciton, default is the id() judge
"""


class Card(object):
    """
    扑克牌类
    """

    def __init__(self, card_type):
        self.card_type = card_type
        # 名称
        self.name = self.card_type.split('-')[0]
        #花色
        self.color = self.card_type.split('-')[1]
        #大小
        self.rank = int(self.card_type.split('-')[2])

    # 判断大小
    def bigger_than(self, card_instance):
        if (self.rank > card_instance.rank):
            return True
        else:
            return False

    def __eq__(self, other):
        return self.card_type == other.card_type


a = [Card("1-a-1") for _ in xrange(5)]
print len(a)
e = Card("1-a-1")
a.remove(e)
print len(a)
