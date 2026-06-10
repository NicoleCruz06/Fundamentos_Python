# -*- coding: utf-8 -*-
"""
Created on Fri May 22 11:22:41 2026

@author: nicole.cruz
"""

lista = []
for contador in range(4):
  num = float(input('Digite um número:').replace(',','.'))
  lista.append(num)
print(lista[::-1])