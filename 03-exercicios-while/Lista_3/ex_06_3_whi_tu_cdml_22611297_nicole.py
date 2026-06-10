# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 08:45:17 2026

@author: nicole.cruz
"""
n = 0 
soma = 0
print('Digite um número positivo caso queira adicioná-lo à soma ou um número negativo para parar.')
while n >= 0:
    n = float(input('Digite um número:').replace(',','.'))
    if n >= 0:
      soma += n 
print('A soma dos números digitados é:%.2f'%soma)
    