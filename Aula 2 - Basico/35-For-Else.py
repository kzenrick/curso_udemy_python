#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 22:37:51 2020

@author: vitorino
"""

variavel = ['Carlos', 'Henrique', 'Rocha', 'Vitorino']

for nome in variavel:
    print(nome, end=', ')
else:
    print('\nFim')
print()

for nome in variavel:
    if nome.startswith('Henr'):
        continue
    elif nome.startswith('Vit'):
        break
    print(nome, end=',')
else:
    print('\nFim')
    
    
# =============================================================================
# Cai no else com lista vazia    
# =============================================================================
#%% vazia
variavel = []

for item in variavel:
    print('tem iten?')
else:
    print('só eu devo ser visto')