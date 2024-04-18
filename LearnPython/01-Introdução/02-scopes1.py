#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 23:09:10 2020

@author: vitorino
"""

# Escopo local vs escopo global
def local():
    n = 7
    print(f'local: {n}')
    
n = 5
print(f'global1: {n}')

local()

def local2():
    print(f'local2: {n}')
    
local2()

def local3():
    try:
        n += 1
        print(f'local3: {n}')
    except UnboundLocalError:
        print('local3: "n" não pode alterar')

local3()
print(f'global2: {n}')
