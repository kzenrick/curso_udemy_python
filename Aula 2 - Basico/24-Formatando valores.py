#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 23:32:31 2019

@author: vitorino
"""

'''
Formatando valore com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Número de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> = Esquerda
< = Direita
^ = Centro
'''

# Inicialização de variáveis
num_1 = 10
num_2 = 3

divisao = num_1 / num_2
nome = 'Carlos'

# String
print('Olá {:s}'.format(nome))
print(f'"{nome}"')
print(f'"{nome:-^15}"')

#inteiro
print(f'{num_1:0>10} e {num_2:0^10}')

# float
print('{:.2f}'.format(divisao))

print(f'{num_2:0>5.2f}')
print(f'{divisao:.2f}')


