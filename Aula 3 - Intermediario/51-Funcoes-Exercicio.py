#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 22:40:58 2020

@author: vitorino
"""

# =============================================================================
# 1. Crie uma função 1 que recebe uma função como parametro e retorne
#    o valor da função2 executada
# =============================================================================

def funcao_1(par):
    return par()

def funcao_2():
    return 2

print(funcao_1(funcao_2))

# =============================================================================
# 2. Crie uma função1 que recebe uma função2 como parametro e retorne 
#    o valor da função2 executada. Faça função1 executar duas funções 
#    que recebam um número diferente de argumentos
# =============================================================================
def funcao_3(*args, **kwargs):
    funcao4 = kwargs.get('funcao_4')
    r1 = funcao4(args[0])
    
    funcao5 = kwargs.get('funcao_5')
    r2 = funcao5(args[1], args[2])
    
    return r1, r2
    
def funcao_a(s):
    return f'<{s}>'
    
def funcao_b(t, u):
    return f'{t} | {u}'
    
print(funcao_3(22, 1, 'w', funcao_4 = funcao_a, funcao_5 = funcao_b))


def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(saudacao, nome):
    return f'{saudacao}, nome'

print(mestre(fala_oi, 'Felipe'))
print(mestre(saudacao, 'Olá', 'Léia'))