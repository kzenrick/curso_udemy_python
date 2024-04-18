#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 23:04:04 2020

@author: vitorino
"""

# =============================================================================
# Exemplo basico
# =============================================================================
a = lambda x, y: x * y
print(a(2, 3))

# =============================================================================
# Uso
# =============================================================================
lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
    ]

print(lista)

# Ordernada por preço
# def func(item):
#    return item[1]

func = lambda i: i[1]

lista.sort(key=func)
print(lista)

# ordem reversa
lista.sort(key=func, reverse=True)
print(lista)

