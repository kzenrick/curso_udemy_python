#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 22:29:07 2020

@author: vitorino
"""

# Cópia simples
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [variavel for variavel in l1] 

l1 == l2

ex2 = [v *2 for v in l1]
ex2

ex3 = [(v, v2) for v in l1 for v2 in range(3)]
ex3

l2 = ['Luiz', 'Mario', 'Maria']
ex4 = [v.replace('a', '@') for v in l2]
ex4

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2')
    )

ex5 = [(v2, v1) for v1, v2 in tupla]
ex5

l3 = list(range(100))
# Mostrar divisíveis por 13
ex6 = [v for v in l3 if v % 13 == 0]
ex6

# Divisíveis por 3 e 8
ex7 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]
ex7

# Usando ELSE
ex8 = [v if v % 3 == 0 else None for v in l3]
ex8

# Usando OR
ex9 = [v if v % 3 == 0 or v%8 == 0 else None for v in l3]
ex9
