#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 23:11:18 2020

@author: vitorino
"""

# =============================================================================
# 1. Crie uma função que exibe uma saudação com os parametros saudação e 
#    nome
# =============================================================================
def funcao(saudacao, nome):
    print(f'{saudacao} {nome}')
    
funcao('oi', 'mundo')

# =============================================================================
# 2. Crie uma função que recebe 3 números como parametros e exeiba a soma
#    entre eles
# =============================================================================
#%% dois
def soma(p1, p2, p3):
    b1 = (type(p1) == int) or (type(p1) == float)
    b2 = (type(p2) == int) or (type(p2) == float)
    b3 = (type(p3) == int) or (type(p3) == float)
    
    if b1 and b2 and b3:
        return p1 + p2 + p3
    else:
        return

valor = soma(1, 2, 3)

if valor:
    print(f'A soma é {valor}')
else:
    print('algum dos valores não é numeral')
    
valor = soma('1', 3, 1)

if valor:
    print(f'A soma é {valor}')
else:
    print('algum dos valores não é numeral')

# =============================================================================
# 3. Crie uma função que receba 2 números. o 1ª é um valor e o segundo
#    um percentual. Retorne o valor do primeiro número somado do aumento
#    do percentual do mesmo
# =============================================================================
#%% tres
def percent(p1, p2):
    b1 = (type(p1) == int) or (type(p1) == float)
    b2 = (type(p2) == int) or (type(p2) == float)
    
    if b1 and b2:
        return p1 * (1 + p2 / 100.00)
    return

calc = percent(33, 66)

if calc:
    print(f'O novo valor é {calc}')
else:
    print('algum dos valores não é numeral')

calc = percent(100, '20')

if calc:
    print(f'O novo valor é {calc}')
else:
    print('algum dos valores não é numeral')
    
    
calc = percent(33, 66.666666)

if calc:
    print(f'O novo valor é {calc}')
else:
    print('algum dos valores não é numeral')
    
# =============================================================================
# 4. Fizz Buzz - Se o parametro da funçaõ for divisível por 3, retorne fizz,
#    se o parametro for divisivel por 5 retorne buzz, se divisivel por
#    3 e 5, retorne FizzBuzz, caso contrário retorne o número enviado
# =============================================================================
#%% quatro
def FizzBuzz(p):
    if type(p) is int or type(p) is float:
        div_3 = (p % 3 == 0)
        div_5 = (p % 5 == 0)
        if (div_3) and (div_5):
            return 'FizzBuzz'
        elif div_3:
            return 'Fizz'
        elif div_5:
            return 'Buzz'
        else:
            return p
        
print(2, FizzBuzz(2))
print(3, FizzBuzz(3))
print(5, FizzBuzz(5))
print(15, FizzBuzz(15))