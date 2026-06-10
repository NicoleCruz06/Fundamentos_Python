# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 11:51:16 2026

@author: nicole.cruz
"""
H = 0
num = int(input('Digite o valor de n:'))
print('Programa para gerar H')
for contador in range(1,(num + 1),1):
    soma = 1/contador
    H += soma
print('O valor de H é:',H)
