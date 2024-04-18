#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 20:20:29 2020

@author: vitorino
"""

# =============================================================================
#%% Multivalor
lista = ['A', 'B', 'C', '3, 2, 1', 2, 1]

for item in lista:
    print(item, end=', ')
    
# =============================================================================
# Acesso via índice -> Negativo conta de trás para frente
# =============================================================================
#%% Indice

print(lista[0], lista[-1])
print(f'"{lista[3]}" => "{lista[-3]}"')

# =============================================================================
# Fatiamento -> O último indíce informado não é incluído no fatiamento
# =============================================================================
#%% Fatiamento
print(lista[2:])
print(lista[2:3])
print(lista[:2])
print(lista[:-3])

# Mostra índices positivos
print(lista[::2])

# Mostra de trás para frente
print(lista[-1:0:-2])

# Lista invertida -> exclui a primeira posição
print(lista[-1:0:-1])

# reverte a própria lista
lista.reverse()
print(lista)

# Volta a lista para original
lista.reverse()
print(lista)

# Imprime a lista invertida sem altera-la
print(lista[::-1])

# =============================================================================
# Alteração na lista
# =============================================================================
#%% Manipulação
# adiciona item ao final da lista
lista.append(99)
print(lista)

# adiciona item a uma posição da lista
lista.insert(3, "Novo 3")
print(lista)

# remove e retorna o útimo elemento da lista
lista.pop()
print(lista)

# remove e retorna um item da lista
lista.pop(3)
print(lista)

# retorna uma cópia da lista
lista_1 = lista.copy()
print(lista_1, '\n', lista)

# Limpa os itens da lista
lista_1.clear()
print(lista_1, '\n', lista)

# Retorna o menor valor de uma lista, mas apenas se do mesmo tipo
print(min(lista[-2:]))
print(min(lista[:-2]))

try:
    print(min(lista[:]))
except:
    print('itens de tipos diferentes')
    
# Retorna o maior valor de uma lista, mas apenas se do mesmo tipo
print(max(lista[-2:]))
print(max(lista[:-2]))

try:
    print(max(lista[:]))
except:
    print('itens de tipos diferentes')

# Outra maneira de apagar um item da lista
lista_1 = ['apague-me', 'a mim não']
print(lista_1)

del(lista_1[0])
print(lista_1)

# Junção de 2 listas, alterando a primeira lista
lista_1.extend(lista)
print(lista_1)

# Outra forma de juntar
lista_2 = [44, 55, 66]
print(lista_2)

print(lista_2 + lista)
print(lista_2, '\n', lista)

# adiciona uma lista a outro item
lista_2.append(lista)
print(lista_2)

# =============================================================================
# Criando lista com range
# =============================================================================
#%% range
lista_3 = list(range(4))
print(lista_3)
