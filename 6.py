#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'soul'
import sys

sys.stdout.write(chr(2))
sys.stdout.write(chr(1))
print('')

for i in range(1,11):
	for j in range(1,i):
		sys.stdout.write(chr(219))
		sys.stdout.write(chr(219))
	print('')