#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 23:34:43 2020

@author: vitorino


-> É uma lista de listas de números inteiros
-> As listas internas tem o tamanho de 10 elementos
-> as listas internas contém números entre 1 a 10 e ele podem ser duplicados

Exercício:
    
-> Crie uma função que encontra o primeiro duplicado na lista interna.
    
    Requisitos
        A ordem do número duplicado é considerada a partir da segunda
        ocorrência (o número duplicado em si).
        Exemplo: 
            [1, 2, 3, 3, 2, 1] : onde todos são duplicados - retorne 3
            [1, 2, 3, 4, 5, 6] : retorne -1
            
        
        Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    [5, 3, 1, 1, 5, 3, 1, 8, 8, 7],
    ]


def menor_indice(lista):
    menor = -1
    for pos, item in enumerate(lista):
        if pos == menor:
            break

        if pos < len(lista) - 1:
            try:
                achado = lista.index(item, pos + 1)
                menor = achado if menor == -1 else min(achado, menor)
            except Exception:
                pass
        
        # print(pos, item, menor)       
        
        
    return menor
    
for i, item in enumerate(lista_de_listas_de_inteiros):
    x = menor_indice(item)
    print(f'{i}. índice duplicado: {x} : {item[x] if x > -1 else None}')
