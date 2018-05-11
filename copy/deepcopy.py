#!/usr/bin/env python
# coding=utf-8
import copy

person = ['name', ['savings', 100.00]]
hubby = person
#wifey = list(person)
wifey = copy.deepcopy(person)

print [id(x) for x in person, hubby, wifey]

print [id(x) for x in hubby]
print [id(x) for x in wifey]


hubby[0] = 'joe'
wifey[0] = 'jane'
print hubby, wifey

hubby[1][1] = 50.00
print hubby, wifey

print [id(x) for x in hubby]
print [id(x) for x in wifey]

print '+'*50
print '只有原子类型的深拷贝'

person = ['name', ('savings', 100.00)]
newPerson = copy.deepcopy(person)
print [id(x) for x in person, newPerson]
print [id(x) for x in person]
print [id(x) for x in newPerson]


print '+'*50
print '包含非原子类型的不可变量的深拷贝', ': 是深拷贝'

person = ['name', ('savings', [1,100.00])]
newPerson = copy.deepcopy(person)
print [id(x) for x in person, newPerson]
print [id(x) for x in person]
print [id(x) for x in newPerson]
print [id(x) for x in person[1]]
print [id(x) for x in newPerson[1]]