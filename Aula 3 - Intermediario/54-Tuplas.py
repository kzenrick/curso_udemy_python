#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 23:04:11 2020

@author: vitorino
"""

# =============================================================================
# Tuplas = Uma lista que não pode ser editada
# =============================================================================
t1 = (1, 2, 3, 4)
print(t1)

try:
    print(t1[1])
    t1[1] = 11
except:
    print('não pode alterar, otário')
    
# acessar os registros da tupla
for v in t1:
    print(v, end=', ')
    
print()

# criar sem os parentes
t2 = 1, 2, 3, 
print(type(t2))

# Concatenar duplas
t3 = t1 + t2
print(t3)

# Desempacotar
a, b, c , *_ = t3 
print(a, b, c, _)

# Converter para listas
l1 = list(t3)
l1[5] = 5
print(t3, l1)