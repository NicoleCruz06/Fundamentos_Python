# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 08:35:01 2026

@author: nicole.cruz
"""
C = 0
F = 32
print('Quais são as 20 primeiras temperaturas a partir de 32F convertidas?')
while C <= 20:
    C = (5/9)*(F-32)
    print('%.2f'%F,'graus fahrenheit convertidos é igual a %.2f'%C,'graus celsius.')
    F += 1.8
    C += 1
    
