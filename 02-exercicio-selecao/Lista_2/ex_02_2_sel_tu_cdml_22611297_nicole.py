# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 08:45:53 2026

@author: nicole.cruz
"""

a = float(input('Digite o valor da primeira variável:').replace(',','.'))
b = float(input('Digite o valor da segunda variável:').replace(',','.'))
if a > b:
    print('O maior valor é',a,'de',a,'e',b,'digitados')
elif b > a:
    print('O maior valor é',b,'de',b,'e',a,'digitados')
else:
    print('Os valores',a,'e',b,'são iguais')

