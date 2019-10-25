#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 13:28:13 2019
@author: brett
"""

x = lambda a : a + 10
print(x(5))
r = 8

x2 = lambda a, b : a * b
print(x(5, 6))

#non-mutator
x(r)
x(r)
a = 4
d = 3
