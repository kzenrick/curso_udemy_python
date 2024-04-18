#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 22:54:50 2020

@author: vitorino
"""

# =============================================================================
# Uso de return em função - se não informado retorna None
# =============================================================================
def funcao(p1, p2):
    return f'{p1}-{p2}'
    # pós return não mostra nada
    print('não será mostrado')

def funcao2(p1, p2):
    print(funcao(p1, p2))
    
print(funcao('oi', 'eu'))

if funcao2('olá', 'vc') is None:
    print('None')
else:
    print('Algum Valor')
    
# =============================================================================
# Ordem Parametro
# =============================================================================
#%% Divisao
def divisao(n1, n2):
    if n2 == 0:
        return 
    return n1 / n2

divide = divisao(8, 1)
if divide:
    print(f'resultado: {divide}')
else:
    print('conta inválida')

# =============================================================================
# Ponteiro para Função
# =============================================================================
#%% Ponteiro
def f(var):
    print(var)
    
def dumb():
    return f

var = dumb()
print(type(var))

var(2)