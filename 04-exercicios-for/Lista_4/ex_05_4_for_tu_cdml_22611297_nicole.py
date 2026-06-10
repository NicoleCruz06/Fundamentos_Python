# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 11:33:47 2026

@author: nicole.cruz
"""
m = 0
print('Tabela de conversão:')
print(' Metros      ->      Pés')
for contador in range(0,101,1):
    if contador == 20:
        input('Digite enter para continuar:')
    elif contador == 40:
        input('Digite enter para continuar:')
    elif contador == 60:
        input('Digite enter para continuar:')
    elif contador == 80:
        input('Digite enter para continuar:')
    pe = m*3.2808
    print('%.2f'%m,'metro(s) --> %.2f'%pe,'pé(s)')
    m += 1

