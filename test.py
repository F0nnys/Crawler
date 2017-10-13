#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/10 0:42
# @Author  : Aries
# @Site    : 
# @File    : test.py
# @Software: PyCharm

def consumer():
    r = None
    while True:
        r = "ok"
        n = yield r
        if not n:
            return
        print("[consumer] consuming %s..." % n)



def produce(c):
    c.send(None)
    n = 0
    while n<5:
        n = n+1
        print("[producer] producing %s" % n)
        l = c.send(n)
        print("[producer] consumer return %s" % l)

    c.close()

c = consumer()
produce(c)

