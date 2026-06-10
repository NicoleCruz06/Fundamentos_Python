# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 10:43:09 2026

@author: nicole.cruz
"""
print('Tabela de conversão valores negativos - Fahrenheit -> Celsius')
F = -459.67
for contador in range (-1,-51,-1):
    C = (5/9)*(F-32)
    print('%.2f'%F,'°F -> %.2f'%C,'°C')
    F += 1.8
    
print('Tabela de conversão valores positivos - Fahrenheit -> Celsius')
F = 32
for contador in range (0,51,1):
    C = (5/9)*(F-32)
    print('%.2f'%F,'°F -> %.2f'%C,'°C')
    F += 1.8
    
