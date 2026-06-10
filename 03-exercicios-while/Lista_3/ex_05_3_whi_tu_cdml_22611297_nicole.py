# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 08:36:06 2026

@author: nicole.cruz
"""
i = -1
n = 0
soma = 1
print('Quando quiser terminar, digite -1')
while n != -1:
    n = float(input('Digite um número:').replace(',','.'))
    i += 1
    soma += n
print('Quantidade de números digitados:',i)
print('A soma dos valores digitados é:',soma)