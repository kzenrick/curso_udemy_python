#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 20:08:21 2020

@author: vitorino
"""

# =============================================================================
# SET - Conjunto mutáveis não ordenados de objetos imutáveis
# =============================================================================

# Manipulações em conjutos SET
small_primes = set()
small_primes.add(2)
small_primes.add(3)
small_primes.add(5)

# verificar itens adicionados
print(small_primes)

# adicionar novo item - ele será ordenado
small_primes.add(1)
print(small_primes)

# remover item
small_primes.remove(1)
print(small_primes)

# verificar se item está no conjunto *set*
3 in small_primes
1 in small_primes

# Não permite adição de item duplicado - Não ocorre exceção
small_primes.add(3)
print(small_primes)

# Criando o conjunto a partir de uma lista # duplicados serão removidos
small_primes = {2, 3, 5, 5, 7, 2}
print(small_primes)

# =============================================================================
# Frozenset - Conjunto imutável : pode ser usado como chave de dicionário
# =============================================================================
small_primes = frozenset([2, 3, 5, 7])
bigger_primes = frozenset([5, 7, 11])

# não pode adicionar itens a um frozenset
small_primes.add(1)

# não pode remover intes de um frozenset
bigger_primes.remove(5)

# pode-se comparar 2 frozenset
small_primes & bigger_primes

# união de 2 frozenset
small_primes | bigger_primes
