#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 15:53:36 2019

@author: vitorino
"""

texto = 'Python 3.7.5'

# Imprime os indices e seus caracteres
j = 0
for i in texto:
    print(f'{j} = "{i}"', end =', ')
    j += 1
print()

# Imprime Python 3
print(texto[:8])

# Imprime .7.5
print(texto[-4:])

# Imprime da posição 3 até a antepenultima
print(texto[3:-3])

# Imprime os caracteres pares
print(texto[::2])

# Imprime os caracteres multiplos de 3
print(texto[::3])
