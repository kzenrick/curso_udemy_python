#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 21:58:10 2020

@author: vitorino
"""

# =============================================================================
# Método Tradicional
# =============================================================================
def func(a1, a2, a3, a4, a5 = None):
    print(a1, a2, a3, a4, a5)
    
func(1, 'a', 2, 'b')


# =============================================================================
# Argumentos Variados
# -> args = desempacota os parametros informados
# =============================================================================
#%% args
def func_1(*args):
    print(type(args), args, len(args))
    
lista = [1, 2, 3, 4, 5]
func_1(lista)
print(*lista)

n1, n2, *n = lista
func_1(n1, n2, n)

func_1(1, 2, 3, 4, 5, 6)

# =============================================================================
# Argumentos com palavras chaves
# =============================================================================
#%% kwargs
def func_2(**kwargs):
    print(kwargs)
    
    # Serve para previnir se foi passado o parametro
    ll = kwargs.get('ll')
    if ll != None:
        print(kwargs['ll'])
    else:
        print('ll não enviado')
    
try:
    func_2(lista)
except:
    print('Não existe argumento - parametro é por palavra chave')
    
func_2()
func_2(ll=lista)