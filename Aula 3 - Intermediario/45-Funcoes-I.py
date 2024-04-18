#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 22:47:26 2020

@author: vitorino
"""
# =============================================================================
# def para declarar função
# =============================================================================
def saudacao(msg, nome):
    print(f'{msg} {nome}')

saudacao('Oi', 'mundo')
saudacao('olá','vc')

# =============================================================================
# Valores Default - quando informado, todos parametros após ele deverá ter
# =============================================================================
def saudacao_1(msg = 'oi', nome = 'eu'):
    saudacao(msg, nome)
    
saudacao_1(nome = 'Eu')
saudacao_1()

saudacao_1('eae')

