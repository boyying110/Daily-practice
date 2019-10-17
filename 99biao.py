#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'soul'

for i in range(1,10):
    for j in range(1,10):
        print(str(j) + ' * ' + str(i) + ' = ' ,j*i , ' ',end='')
        if(i == j ):
           print()
           break


for i in range(9,0,-1):
    for j in range(1,i+1):
        print(str(j) + ' * ' + str(i) + ' = ' ,i*j , ' ',end='')

    print()



