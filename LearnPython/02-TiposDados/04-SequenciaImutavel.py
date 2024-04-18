#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 22:30:52 2020

@author: vitorino
"""

# =============================================================================
# Encoding/Decoding Strings 
# =============================================================================
s = "This is üŋíc0de"  # unicode string: code points
type(s)

encoded_s = s.encode('utf-8')  # utf-8 encoded version of s
encoded_s

type(encoded_s)  # another way to verify it

encoded_s.decode('utf-8')  # let's revert to the original

bytes_obj = b"A bytes object"  # a bytes object
type(bytes_obj)
print(bytes_obj)

# =============================================================================
# Indexing e Slicing
# =============================================================================
s = 'Esse é uma frase para testes de string'
s[0] # Índice inicia a contar do 0
s[5] # Índice 5, 6ª posição
s[:4] # Início do arquivo, até o quarto índice não incluso
s[4:] # Índice 4 inclusice, até o final
s[11:16] # Índice 11 inclusive, até a 16 excluido
s[11:16:2] # Idem ao anterior, pulando de 2 em 2 caracteres

# =============================================================================
# Formatando strings
# =============================================================================
# Combinando strings
a = 'Olá %s'
a % 'Mundo'

s = 'texto 1'; t = 'texto 2'
'meus %s %s' % (s, t)

# uso de formato
m = 'meus {} e {}'
m.format(s, t)

# uso format e indices
m1 = 'meus {1} e {0}'
m1.format(s, t)

# uso format e nomes
m2 = 'meu {t1} e {t2}'
m2.format(t2=s, t1=t)

# formatação literal
f'meu {s} {t}'

# =============================================================================
# Tuplas
# =============================================================================
# Criação de tuplas
t = ()

um_elemento = (4, ) # precisa de vírgula no final qdo tem uma vírgula
tres_elementos = (3, 4, 5) # parenteses são opcionais
nova_tupla = 3, 4 , 5
type(nova_tupla)
nova_tupla

a, b, c = 1, 2, 3 # tuplas para múltiplas atribuições
a, b, c # tupla ímplicita para imprimir em uma instrução

a, b = 1, 2, 3 # Erro 

# Verificar item em uma tupla
3 in tres_elementos

# Troca de variáveis com 1 linha
a, b = 1, 2
a, b = b, a
a,b

