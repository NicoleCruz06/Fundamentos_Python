# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 11:19:25 2026

@author: nicole.cruz
"""
import os
print('Tabela de conversão valores negativos - Fahrenheit -> Celsius')
F = -459.67
for contador in range (-1,-51,-1):
    if contador == -24:
        input('Digite enter caso deseje continuar:')
    C = (5/9)*(F-32)
    print('%.2f'%F,'°F -> %.2f'%C,'°C')
    F += 1.8
    
print('Tabela de conversão valores positivos - Fahrenheit -> Celsius')
F = 32
for contador in range (0,51,1):
    if contador == 26:
        input('Digite enter caso deseje continuar:')
    C = (5/9)*(F-32)
    print('%.2f'%F,'°F -> %.2f'%C,'°C')
    F += 1.8
