#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 22:53:05 2020

@author: vitorino
"""

nome = input('Diga nome: ')

if nome:
    print(nome)
else:
    print('falow ou ninguém')
    
# Outro jeito de escrever
erro = 'falow ou ninguém'
print(nome or erro)

a = 0
b = None
c = False
d = []
e = {}
f = ()
g = ''
h = 21
i = 'Nao imprime'

print(a or b or c or d or e or f or g or h or i)

print(c or d or a or i or h or g)