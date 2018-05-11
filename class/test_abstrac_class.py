#!/usr/bin/env python
# coding=utf-8
__author__ = 'Qingwei'

from abc import ABCMeta, abstractmethod


class Book:
    __metaclass__ = ABCMeta

    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display(): pass


class MyBook(Book):
    def __init__(self, title, author, price):
        super(MyBook, self).__init__(title, author)
        self.price = price;
    def display(self):
        print "Title: %s"%self.title
        print "Author: %s"%self.author
        print "Price: %d"%self.price

title = raw_input()
author = raw_input()
price = int(raw_input())
new_novel = MyBook(title, author, price)
# a = Book(title, author)
new_novel.display()