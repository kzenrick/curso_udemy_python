#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 22:32:04 2020

@author: vitorino
"""

perguntas = {
    'Pergunta 1:' : {
        'pergunta' : 'Quanto é 2+2?',
        'respostas': {
            'a': 1,
            'b': 4,
            'c': 5,
            }, # fim respostas
        'resposta_certa': 'b',
        }, # fim pergunta 1
        
    'Pergunta 2:' : {
        'pergunta' : 'Quanto é 3*2?',
        'respostas': {
            'a': 4,
            'b': 10,
            'c': 6,
            }, # fim respostas
        'resposta_certa': 'c',
        }, # fim pergunta 2
    } # fim perguntas

for p_num, perg in perguntas.items():
    print(f'{p_num} {perg["pergunta"]}')
    
    for resp_let, resp_valor in perg['respostas'].items():
        print(f'[{resp_let}]: {resp_valor}')
        
    rs_user = input('Resposta Certa: ')
    
    if rs_user == perg['resposta_certa']:
        print('Ok')
    else:
        print('errou! Resposta correta: ', perg['resposta_certa'])
        
    print()