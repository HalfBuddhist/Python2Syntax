#!/usr/bin/env python
# coding=utf-8

class HotelRoomCalc(object):
    'Hotel room rate calculator'
    def __init__(self, rt, sales=0.085, rm=0.1):
        '''HotelRoomCalc default arguments: sales tax == 8.5% and room tax == 10%'''
        self.salesTax = sales
        self.roomTax = rm
        self.roomRate = rt

    def calcTotal(self, days=1):
        'Calculate total; default to daily rate'
        daily = round((self.roomRate * (1 + self.roomTax + self.salesTax)), 2)
        return float(days) * daily

sfo = HotelRoomCalc(299) # new instance 新的实例
print sfo.calcTotal() # daily rate 日租金
# 354.32
print sfo.calcTotal(2) # 2-day rate ２天的租金
# 708.64
sea = HotelRoomCalc(189, 0.086, 0.058) # new instance 新的实例
print sea.calcTotal()
# 216.22
print sea.calcTotal(4)
# 864.88
wasWkDay = HotelRoomCalc(169, 0.045, 0.02) # new instance 新实例
wasWkEnd = HotelRoomCalc(119, 0.045, 0.02) # new instance 新实例
print wasWkDay.calcTotal(5) + wasWkEnd.calcTotal() # 7-day rate 7 天的租金
# 1026.69