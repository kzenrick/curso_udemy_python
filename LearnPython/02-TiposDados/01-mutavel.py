#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 23:39:57 2020

@author: vitorino
"""

# Posições de memória


class Person():
    def __init__(self, age):
        self.age = age

fab = Person(42)
print(fab.age)

id(fab)

id(fab.age)

fab.age = 25

id(fab)

id(fab.age)


l = 14
id(l)

l += 1
id(l)

l = 22
id(l)
