#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 22:16:59 2019

@author: vitorino
"""


def par_ou_impar():
    '''
    Faça um programa que peça ao usuário para digitar um número inteiro,
    informe se este número é par ou ímpar. Caso o usuário não digite um número
    inteiro, informe que não é um número inteiro.
    '''

    valor = input("Informe um número: ")

    try:
        # pode-se usar valor.isdigit() para não ter exceção 
        i = int(valor)

        if i % 2 == 0:
            print(f'{valor} é um número par')
        else:
            print(f'{valor} é um número escolhido é impar')
    except ValueError:
        print(f'{valor} não é um inteiro válido')


def saudacao():
    '''
    Faça um programa que pergunte a hora do usuário e, baseando-se no horário
    descrito, exiba a saudação apropriada. Ex.
    Bom dia 0-11, Boa tarde 12-17 e Boa noite-18-23
    '''

    valor = input('Que horas são (valor entre 0 e 23): ')

    try:
        # pode-se usar valor.isdigit() para não ter exceção
        i = int(valor)

        if (i < 0) or (i > 23):
            print('Horas deve ser um inteiro entre 0 e 23')
        elif i <= 11:
            print('Bom dia')
        elif i <= 17:
            print('Boa tarde')
        else:
            print('Boa noite')
    except ValueError:
        print(f'{valor} não é um inteiro válido')


def diga_seu_nome():
    '''
    Faça um programa que peça o primeiro nome do usuário.
    Se o nome tiver 4 letras ou menos escreva "Seu nome é curto";
    se tiver entre 5 e 6 letras, escreva  "Seu nome é normal";
    maior que 6 escreva "Seu nome é muito grande".
    '''

    valor = input('Diga seu nome: ')

    if len(valor) <= 4:
        print('Seu nome é curto')
    elif len(valor) <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é grande')


if __name__ == '__main__':
    par_ou_impar()
    saudacao()
    diga_seu_nome()
