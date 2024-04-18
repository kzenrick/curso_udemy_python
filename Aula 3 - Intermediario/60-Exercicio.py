#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 22:51:24 2020

@author: vitorino
"""

string = '0123456789' * 6
string

# Montar uma lista com os grupos de 0 a 9
lista = [string[i:i+10] for i in range(0, len(string), 10)]
lista

# Concatenar a lista e juntar com ponto
retorno = '.'.join(lista)
retorno
