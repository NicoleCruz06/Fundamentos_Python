# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 08:35:18 2026

@author: nicole.cruz
"""
print('Conversão Fahrenheit-Celsius')
F = float(input('Insira o valor inicial da temperatura em fahrenheit:').replace(',','.'))
F_final = float(input('Insira o valor final da temperatura em fahrenheit:').replace(',','.'))
while F <= F_final:
    C = (5/9)*(F-32)
    print('%.2f'%F,'graus fahrenheit convertido é %.2f'%C,'graus celsius.')
    F += 1.8
