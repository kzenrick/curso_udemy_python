#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 20:50:39 2019

@author: vitorino
"""

i = 0

while i != 1:
    x = input('[1] sai while - [0] break: ')

    if x.isdigit():
        i = int(x)
        if i == 0:
            break
else:
    print('Apenas se [1] foi digitado')

print('Fim')
