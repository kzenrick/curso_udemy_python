#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 22:06:59 2020

@author: vitorino
"""

# =============================================================================
# split - quebra um texto em uma lista, escolhendo um separador
# =============================================================================
#%% split
string = 'O Brasil é o país do futebol, o Brasil é penta.'
lista = string.split()
print(lista)

print(lista == string.split(' '))

lista_2 = string.split(',')
print(lista_2)

lista_3 = string.split('o')
print(lista_3)

for valor in lista:
    print(f'{valor} apareceu {lista.count(valor)}')
    
# =============================================================================
# Join - juntar uma lista para formar uma string
# =============================================================================
#%% join
string_2 = ' '.join(lista)
print(string_2)

# =============================================================================
# enumerate - enumerar os elementos da lista
# =============================================================================
#%% enumerar
for v1, v2 in enumerate(lista):
    print(f'{v1}º = {v2}')
    
x = [
     [1, 'nome1'],
     [2, 'kolos'],
     [3, 'lsado']
     ]

for i, n in x:
    print(i , n)
    
# desempacotar em várias variaveis
x = ['abc', 'dfe', 'hjs']
x1, x2, x3 = x
print(x1, x2, x3)

# Se a quantidade não bater... tá exceção
x1, x2 = x

