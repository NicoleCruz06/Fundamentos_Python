# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 15:16:15 2026

@author: nicole.cruz
"""
lista = []
def potencia(x,y):
    return(lista**lista.index)
for contador in range(20):
   x = int(input(f'Digite um número inteiro para ser a base de uma potência elevada a {contador+1}:'))
   lista.append(x)

print('------ Lista de potências ------')
for contador in range(20):
    print(f'{lista[contador]} elevado a {contador} é igual a {potencia(x,y)}')
