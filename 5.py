#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'soul'

import sys
for i in range(8):
    for j in range(8):
        if ( i + j ) % 2 == 0:
            sys.stdout.write(chr(218))
            sys.stdout.write(chr(219))
        else:
            sys.stdout.write(' ')
    print('')