#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 00:39:15 2020

@author: vitorino
"""

# =============================================================================
# Listas
# =============================================================================
# ----------------------------
# Criar a lista
l = []
l1 = list()

l == l1
l2 = [1,2,3]

# Soma na lista
s = [x + 5 for x in [2,3,4]]
print(s)

# Converter tupla em lista
t = list((1,3,5,7))
type(t)

t

# ----------------------------
# adicionar item a fim da fila
a = [1, 2, 1, 3]
a.append(13)

# contar itens na lista
a.count(1)

# Extender a lista por outra
a.extend([5, 7])
a

# Procura o indice de um item
a.index(13)
a.index(8)

# Para verificar se um item está na lista sem retornar exceção
x = 11
print(-1 if not x in a else a.index(x))
x = 3
print(-1 if not x in a else a.index(x))


# Inserir item na primeira posição
a.insert(0, 17)
a

# Remover e retornar o último elemento
a.pop()

# lista pós-remoção
a

# remover um elemento da posição específica
a.pop(3)

# lista pós-remoção
a

# Remover item específico
a.remove(17)
a

# Inverter a ordem da lista
a.reverse()
a

# Ordenar a lista
a.sort()
a

# Remover todas a lista
a.clear()
a

# =============================================================================
# Listas Heterogeneas
# =============================================================================
a = list('hello')
a

a.append(100)
a

# Extender a lista usando tuplas
a.extend((1,2,3))
a

# Extender usando string
a.extend('...')
a

# adiciona uma lista a outra lista
a.append((3, 2, 1))
a
a[-1]

# =============================================================================
# Funções em listas
# =============================================================================
a = [1, 3, 5, 7]

# Minimo
min(a)

# Maior
max(a)

# Soma
sum(a)

# tamanho da lista
len(a)

# Concatenação de listas
b = [6,7,8]
a + b

# Duplicar a lista
a * 2

# =============================================================================
# Ordenação
# =============================================================================
from operator import itemgetter
a = [(5, 3), (1, 3), (1, 2), (2, -1), (4, 9)]

sorted(a)

sorted(a, key=itemgetter(0))

sorted(a, key=itemgetter(0,1))

sorted(a, key=itemgetter(1))

sorted(a, key=itemgetter(1, 0))

sorted(a, key=itemgetter(1), reverse=True)


# =============================================================================
# Byte Array
# =============================================================================
# Cria um bytearray vazio
a = bytearray()
a

# Cria uma lista com 10 elementos, zerados
a = bytearray(10)
a

# Byte array a partir de um iterable de inteiros
a = bytearray(range(5))
a
a[3]

# bytearray a partir de bytes
name = bytearray(b'Lina')
name

name.replace(b'L', b'l')
name

name.endswith(b'na')

name.upper()

name.count(b'L')
