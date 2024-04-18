#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 23:09:05 2020

@author: vitorino
"""

'''
Dados os números do CPF
    cada 1 dos 9 primeiros registros multiplica pelos valores de 10 a 2
    soma os valores resultante 
    11 - (modulo resultante por 11) 
    valor obtido é o primeiro dígito verificador, zero se maior q 9
    
    Para o segundo digito:
    cada 1 dos 9 primeiros registros multiplica pelos valores de 11 a 3
    o digito 1 encontrado acima multiplica por 2
    soma os valores resultante
    11 - (modulo resultante por 11)
    valor obtido para o segundo digito, zero se valor maior do que 9
'''

cpfs = '78202655153', '16899535009', '78202655156', '81877211802', \
    '11111111111', '22222222222', '10101010101'

for cpf in cpfs:
    novo = cpf[:-2]
        
    while len(novo) < len(cpf):
        soma = 0
        inicio = len(novo) + 1
        
        for i in novo:
            soma += int(i) * inicio
            inicio -= 1
            
        digito = 11 - (soma % 11)
        digito = 0 if digito > 9 else digito
        
        novo += f'{digito}'
        
    print(f'{novo} == {cpf} | {novo == cpf}')
            
        