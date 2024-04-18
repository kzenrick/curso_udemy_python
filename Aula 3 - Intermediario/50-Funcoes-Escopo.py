#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 22:25:47 2020

@author: vitorino
"""

# =============================================================================
# Escopo publico
# =============================================================================
#%% pub
variavel = 'valor'

def func():
    print(f'1. {variavel}')
    
def func_1():
    variavel = 'outro'
    print(f'2. {variavel}')
    
def func_2():
    global variavel
    variavel = 'xunxo'
    print(f'4. {variavel}')
    
    
func()

func_1()    
    
print(f'3. {variavel}')

func_2()
func()
func_1()

print(f'5. {variavel}')

# =============================================================================
# Criar função global dentro de função
# =============================================================================
#%% glb
def nao_funciona():
    teste = 'Nada faz'
    
def da_erro():
    print(teste)
    
try:
    print('a. nao_funcioa')    
    nao_funciona()
    
    print('b. da_erro')
    da_erro()
    
    print('fim')
except:
    print('deu erro acima')
    
def nova_global():
    global my_var
    my_var = 'nova_global'
    
def da_certo():
    print(my_var)
    
try:
    print('nova_global')
    nova_global()
    
    print('da_certo()')
    da_certo()
    
    print('fim')
except:
    print('algo deu errado')