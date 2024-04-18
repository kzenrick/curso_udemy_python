#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 23:09:45 2020

@author: vitorino
"""

# =============================================================================
# Listas com chaves não repetidas
# =============================================================================
#%% criando
s1 = {1,2,3,4,5}
print(s1)

# Não tem como acessar um valor pelo índice
try:
    print(s1[0])
except:
    print('Sem acesso')
    
# Set vazio
s1 = set()
s1.add(1)
s1.add(2)

try:
    s1.add(*(3, 4, 5))
except:
    print('não pode')
else:
    print(s1)

s1.add((3, 4, 5))
print(s1)

# A ordem não é respeitada
s1.update((6, 7, 8))
print(s1)

# =============================================================================
# Usar set para remover itens duplicados de uma lista
# =============================================================================
#%% dupl
l1 = [11, 1, 6, 7, 4, 5, 6, 7, 9, 7, 8, 5, 4, 3, 3, 8, 5, 6]
print('ComDupl:', l1)
print('SemDupl:', list(set(l1)))

# =============================================================================
# União
# =============================================================================
s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 4, 5, 6, 7}
print('s1:',s1,
      '\ns2:', s2,
      '\n|:', s1 | s2 , s2 | s1,    # União
      '\n&:', s1 & s2, s2& s1,      # interseção
      '\n-:', s1 - s2, s2 - s1,      # diferença
      '\n^:', s1^s2, s2^s1,
      )

# =============================================================================
# Exemplo
# =============================================================================
#%% ex
l1 = ['Luiz', 'João', 'Maria']
l2 = ['João', 'Maria', 'Maria', 'Luiz', 'Luiz', 'Luiz', 'Maria', 'João']
l3 = l2.copy()
l3.append('Fulano')

print(l1 == l2)
print(set(l1) == set(l2))

print(set(l3) - set(l2))