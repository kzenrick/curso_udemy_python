#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 00:00:06 2020

@author: vitorino
"""

# pi
pi = 3.1415926536
radius = 4.5
area = pi * (radius ** 2)

print(area)

# =============================================================================
# # Informações sobre pontos flutuantes
# =============================================================================
import sys
sys.float_info

2 ** 64 == 18_446_744_073_709_551_616

# =============================================================================
# # Problema de conversão
# =============================================================================
0.3 - .1 * 3

# O problema como decimal
from decimal import Decimal
Decimal(0.3) - Decimal(0.1) * 3

# Melhora com o uso de string
Decimal('0.3') - Decimal('0.1') * 3 

int(0.3 - 0.1 * 3)

# =============================================================================
# # Numeros Complexos
# =============================================================================
c = 3.14 + 2.73j
c.real
c.imag
c

# O conjugate de A + Bj é A - Bj
c.conjugate()
c * 2

# =============================================================================
# Fração
# =============================================================================
from fractions import Fraction
Fraction(10, 6)

Fraction(1,3) + Fraction(2,3)

f = Fraction(10, 6)
f.numerator
f.denominator


# =============================================================================
# # Decimais
# =============================================================================
from decimal import Decimal as D
D(3.15)
D('3.15')

D('1.4')
D('1.4').as_integer_ratio()

x = D('1.4').as_integer_ratio()
type(x)
x, x[0], x[1]
