#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 22:41:31 2020

@author: vitorino
"""

logado = True

if logado:
    msg = 'Sucesso'
else:
    msg = 'Não sucesso'

print(msg)

# =============================================================================
# Convertendo exemplo acima para ternario
# =============================================================================
msg = 'Sucesso' if logado else 'Não logado'
print(msg)

for idade in [17, 18]:
    msg = f'{idade} '
    msg += ('Não ' if idade < 18 else '') + 'acesso!' 
    print(msg)
