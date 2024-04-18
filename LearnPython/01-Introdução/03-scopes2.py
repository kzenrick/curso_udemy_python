#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 23:17:21 2020

@author: vitorino
"""

# Escopos Local, Enclosing e Global

def enclosing_func():
    m = 13
    
    def local():
        # Tentativa de alterar a variável irá gerar erro, mas posso ler
        # m += 1
        print(f'Enclosing: {m}')
    
        
    local()
    print(f'local: {m}')
    
m = 7

print(f'global: {m}')

enclosing_func()