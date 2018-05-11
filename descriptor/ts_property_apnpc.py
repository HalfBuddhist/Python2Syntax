#!/usr/bin/env python
# coding=utf-8
"""
APNPC(ActiveState Programmer Network Python Cookbook)
(http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/205183)上的一条精明的办
法解决了以下问题：
 “借用”一个函数的名字空间
 编写一个用作内部函数的方法作为 property()的(关键字)参数
 (用 locals())返回一个包含所有的(函数/方法)名和对应对象的字典
 把字典传入 property()，然后
 去掉临时的名字空间APNPC(ActiveState Programmer Network Python Cookbook)
(http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/205183)上的一条精明的办
法解决了以下问题：
 “借用”一个函数的名字空间
 编写一个用作内部函数的方法作为 property()的(关键字)参数
 (用 locals())返回一个包含所有的(函数/方法)名和对应对象的字典
 把字典传入 property()，然后
 去掉临时的名字空间

 可是这样是行不通，提示在初始化时can't set attribute: AttrubuteArror.
 我认为事情是这样的，首先发现有x = property(x)这样的语句，而这是由装饰符等价而来的，
 所以，就会认为是该变量是有实例属性描述符的，而赋值操作会调用其fset函数，而property其实并没有对其做任何的装饰，
 较标准的装饰函数而言，他连一个返回函数指针的语句都没有，还有下面的等式绝对不会是等价的。
 x = property(x)
 x = property(**x())
 而上面才是装饰符正确的等价，如此看来报错也就是必然的了。
 修正方法，不采用修饰符，而采用x = property(**x())这种直接赋值的形式, 这样用实例属性将同名的方法给覆盖了，
 因此对于类的命名空间没有任何的影响。
"""

class HideX(object):
    def __init__(self, x):
        self.x = x

    # @property
    def x():
        def fget(self):
            return ~self.__x
        def fset(self, x):
            assert isinstance(x, int), '"x" must be an integer!'
            self.__x = ~x
        return locals()
    x = property(**x())



############### test intit ###############
# HideX._HideX__x()
print HideX.__dict__
inst = HideX(20)
print inst.x
print type(HideX)
# inst.x()
# 20
############### test set ###############
# inst.x = 30
# print inst.x
# 30

############### 没有强制使用property()，因为它允许对属性方法的访问(由于在类定义中包含属性方法): ###############
# inst.set_x(40) # can we require inst.x = 40?
# print inst.x
# 40