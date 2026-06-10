# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 08:46:03 2026

@author: nicole.cruz
"""

a = float(input('Digite um número qualquer:').replace(',','.'))
if a > 0:
    print('O número',a,'é positivo, e o seu dobro é',2*a)
elif a < 0:
    print('O número',a,'é negativo, e o seu triplo é',3*a)
else:
    print('O número',a,'é nulo')