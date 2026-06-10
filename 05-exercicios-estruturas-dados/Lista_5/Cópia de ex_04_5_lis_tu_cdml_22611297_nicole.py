# -*- coding: utf-8 -*-
"""
Created on Fri May 22 11:21:52 2026

@author: nicole.cruz
"""

lista_1 = []
lista_2 = []
lista_3 = []
for contador in range(10):
  num_1 = float(input(f'Digite um número para a posição {contador} da lista 1:').replace(',','.'))
  num_2 = float(input(f'Digite um número para a posição {contador} da lista 2:').replace(',','.'))
  soma = num_1 + num_2
  lista_1.append(num_1)
  lista_2.append(num_2)
  lista_3.append(soma)
print('------ Somas dos valores da lista 1 + lista 2 ------')
for contador in range(10):
  print(f'A soma de {lista_1[contador]} + {lista_2[contador]} é = {lista_3[contador]}')