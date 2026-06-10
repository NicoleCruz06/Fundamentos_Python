# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 11:07:31 2026

@author: nicole.cruz
"""
n_inicial = int(input('Digite o valor do número inicial da sequência:').replace(',','.'))
n_final = int(input('Digite o valor do número final da sequência:').replace(',','.'))
print('Números entre',n_inicial,'e',n_final)
for contador in range(n_inicial,n_final):
    if n_inicial > n_final:
        print(contador)
        contador -= 1
    elif n_inicial < n_final:
        print(contador)
        contador += 1