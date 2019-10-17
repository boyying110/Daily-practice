#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'soul'

ll=[]
for i in range(0,3):
    a = int(input("please enter number :"))
    ll.append(a)
ll.sort(reverse=True)
print( ll )