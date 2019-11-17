#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 16:12:39 2019

@author: vitorino
"""

'''
Imprimir Coordenadas

Solicita um número de linhas
Solicita um número de colunas
'''


def informe(opcao):
    while True:
        num_1 = input(f"Digite o número de {opcao} (<= 0 para parar): ")

        if not num_1.isdigit():
            print(f'{num_1} não é um número válido\n\n')
            continue
        else:
            valor = int(num_1)

            if valor > 10:
                print(f'{valor} não pode ser maior que 10')
            else:
                return valor


while True:
    max_x = informe('linhas')

    if max_x <= 0:
        print('bye bye')
        break

    max_y = informe('colunas')

    if max_y <= 0:
        print('bye bye')
        break

    x = 0
    while x < max_x:
        y = 0

        while y < max_y:
            print(f'({x},{y})', end='\t')
            y += 1

        x += 1
        print()
