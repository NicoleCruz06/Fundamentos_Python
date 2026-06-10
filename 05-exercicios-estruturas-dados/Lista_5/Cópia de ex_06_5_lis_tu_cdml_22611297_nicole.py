# -*- coding: utf-8 -*-
"""
Created on Fri May 22 11:21:34 2026

@author: nicole.cruz
"""

lista_a = []
lista_b = []
lista_c = []
for contador in range(10):
  num_a = float(input(f'Digite um número para a posição {contador} da lista a:').replace(',','.'))
  lista_a.append(num_a)
for contador in range(20):
  num_b = float(input(f'Digite um número para a posição {contador} da lista b:').replace(',','.'))
  lista_b.append(num_b)
for contador in range(len(lista_a)):
  soma = lista_a[contador] + lista_b[contador]
  lista_c.append(soma)
for contador in range(9,19):
  num_b = lista_b[contador]
  lista_c.append(num_b)

print('------ Somas dos valores da lista a + lista b ------')
print('Lista a:',lista_a)
print('Lista b:',lista_b)
print('Lista c:',lista_c)