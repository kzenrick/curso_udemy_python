#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 22:37:48 2020

@author: vitorino
"""

x = 10
y = '"Eu mesom"'
print(x, y)

x, y = y, x
print(x, y)

print()
z = '"Outro valor"'
print(x, y, z)
x, y, z = z, x, y
print(x, y, z)