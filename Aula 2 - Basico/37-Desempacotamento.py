#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 22:28:53 2020

@author: vitorino
"""

# =============================================================================
# Desempacotamento de Lista
# =============================================================================
lista = ['Luiz', 'João', 'Maria']
n1, n2, n3 = lista
print(n2)

# para recupear menos variáveis do que tem na lista
# jogar demais registros para outra lista
lista.extend(['Gabriel', 'Amanda', 'Felipe', 'Julia', 'Isadora', 'Bia'])
print(lista)

n1, n2, *demais = lista

print(n1)
print(demais)

# Recupera o ultimo
n1, n2, *demais, ultimo = lista
print(ultimo)
print(demais)

# pega os ultimos 3 em variaveis
*demais, n1, n2, n3 = lista
print(demais)
print(n1, n2, n3)
