#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 23:24:47 2020

@author: vitorino
"""

# Ler atributos de classes

class Bike:
    def __init__(self, colour, frame_material):
        self.colour = colour
        self.frame_material = frame_material


    def brake(self):
        print('breaking!')
        
# Criar as instancias
red_bike = Bike('red', 'Carbon fiber')
blue_bike = Bike('blue', 'Steel')

# verificar as variáveis das bicicletas
print(red_bike.colour)
print(blue_bike.frame_material)

# alterar a cor do objeto
red_bike.colour = 'pink'
red_bike.colour

red_bike.brake()
