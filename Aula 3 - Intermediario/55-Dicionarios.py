#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 19:50:44 2020

@author: vitorino
"""

# =============================================================================
# Formas de Criar Dicionário
# =============================================================================
d0 = {'chave1':'valor_da_chave1'}
d0['nova_chave'] = 'Valor da Nova Chave'

print('d0 = ', d0)

try:
    d1['Chave0'] = 0
    print(d1)
except:
    print('Não é assim que se cria d1')

d2 = dict()
d2['Chave[0'] = 0
print('d2 = ', d2)

# =============================================================================
# Acessar o valor do Dicionário
# =============================================================================
print('Chave de d2: ', d2['Chave[0'])

# =============================================================================
# Tipos de índices
# =============================================================================
d3 = {
      'str' : 'Texto',
      123: 'Inteiro',
      (1, 2, 3, 4): 'Tupla'
      }

print('d3[(1,2,3,4)]: ', d3[(1, 2, 3, 4)])

# =============================================================================
# Acesso a chave inexistente
# =============================================================================
#%%inx
try:
    print('d3[1234]: ', d3[1234])
except:
    print('Chave 1234 não existe em d3')
    
# Formas de acessar
# 1. Verificar se existe
if not 1234 in d3:
    print('adicionar valor a chave 1234')
else:
    print('d3[1234]: ', d3[1234])
    
#2. Usando get
print('d3[1234]: ', d3.get(1234))
print('d3[123]: ', d3.get(123))

# =============================================================================
# Atualizar valor dicionário
# =============================================================================
#%% upd
# 1. Acesso direto a chave
d3[1234] = 'Inteiro e Numérico'
print(d3.get(1234))

# Comando update
# Cria uma nova chave
d3.update({'(1, 2, 3, 4)': 'Tuplae nem lista, mas str'})

# Atualiza a existente
d3.update({(1, 2, 3, 4): 'Tupla, mas não lista !!!'})
print('d3.get((1, 2, 3, 4)): ', d3.get((1, 2, 3, 4)))

print('\n', d3)

# Mais uma forma de adicionar
d3.update(apague='12334')
print(d3)


# =============================================================================
# Remoção
# =============================================================================
#%% remocao
del(d3['apague'])

print(d3)

# =============================================================================
# Verificar se valores existem
# =============================================================================
#%% exis
print((1, 2, 3, 4) in d3)
print(21345 in d3)
print('Inteiro' in d3.values())

# =============================================================================
# Correr o Dicionário
# =============================================================================
#%% corr
print('\n Cada item do dicionário no formato de tupla')
for k in d3.items():
    print(k)
    
print('\n Cada item do dicionário no formato desacoplado')
for k, v in d3.items():
    print(k, ' => ', v)

print()    
    
clientes = {
    'cliente1' : {
        'nome': 'Carlos',
        'sobrenome':'Vitorino',
        },
    'cliente2' : {
        'nome': 'Léia',
        'sobrenome': 'Rodrigues',
        },
    }

for k, v in clientes.items():
    print(f'Imprimindo {k}:')
    for w, x in v.items():
        print(f'\t{w:10}\t:\t{x}')
        
        
# =============================================================================
# Referencia de Dicionarios
# =============================================================================
#%% ig
d1 = {1 : 'a', 2: 'b', 3: 'c'}
v = d1

print('Antes:', d1, v)

v[1] = 'p'

print('Depois:', d1, v)

c = d1.copy()
c[1] = 'w'
print('Copy:', d1, c)

d1 = {1: 'a', 2:'b', 3:'c', 'd': ['Meu', 'Nome']}
v = d1.copy()

print(' - ' * 5, '\n', '\nV:' , v, '\nD1:' , d1)

v[1] = 'Diferente'
v['d'][0] = 'Iguais'

print('\nV:' , v, '\nD1:' , d1)

# Cópia totalmente diferente
import copy
v = copy.deepcopy(d1)

v[1] = 'Diferente'
v['d'][0] = 'Não Iguais'

print('\nV:' , v, '\nD1:' , d1)

# =============================================================================
# Recuperar e remover
# =============================================================================
#%%pop
d3 = {
      'str' : 'Texto',
      123: 'Inteiro',
      (1, 2, 3, 4): 'Tupla'
      }

d3[1234] = 'NovoValor'
d3['UltimoItem'] = 'Adios'

print(d3)
w = d3.pop(1234)
print(d3)
print('ItemRemovido: ', w, '\n')

w = d3.popitem()
print(d3)
print('ItemRemovidoII:', w)

# =============================================================================
# Junção de Dicionários
# =============================================================================
#%% jun
d1 = {
      1 : 'a',
      2 : 'b',
      3 : 'c'
     }

d2 = {
      25 : 'x',
      26 : 'y',
      27 : 'z',
      }

d1.update(d2)

print(d1, '\n', d2)