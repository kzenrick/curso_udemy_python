#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 21:00:21 2019

@author: vitorino
"""
import unicodedata


while True:
    frase = input('Digite a frase: ')

    if not frase.strip():
        break

    frase = frase.lower()
    frase = unicodedata.normalize('NFKD', frase)

    contagem_atual = 0
    letra = ''
    tamanho = len(frase)
    c = 0

    while c < tamanho:
        qtd_letras = frase.upper().count(frase[c].upper())

        if qtd_letras > contagem_atual and frase[c].strip():
            letra = frase[c].upper()
            contagem_atual = qtd_letras

        c += 1

    print(f'{letra}: {contagem_atual}')

print('- = F I M = -')
