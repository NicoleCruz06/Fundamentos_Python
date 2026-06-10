# -*- coding: utf-8 -*-
"""
Created on Fri May 22 09:50:57 2026

@author: nicole.cruz
"""
lista_1 = []
lista_2 = []
lista_op = []
lista_resultados = []

for contador in range(20):
    num_1 = float(input(f'Digite o número pertencente a posição {contador + 1} da lista 1:').replace(',','.'))
    lista_1.append(num_1)
    num_2 = float(input(f'Digite o número pertencente a posição {contador + 1} da lista 2:').replace(',','.'))
    lista_2.append(num_2)
    operador = input(f'Digite (+,-,/,*), operação que ocorrerá entre os números de posição {contador + 1} da lista 1 e 2: ')
    lista_op.append(operador)
    
    if operador == '+':
        resultado = (num_1 + num_2)
    elif operador == '-':
         resultado = (num_1 - num_2)
    elif operador == '*':
         resultado = (num_1 * num_2)
    elif operador == '/':
        if num_2 != 0:
           resultado = (num_1 / num_2)
        else:
           resultado = 'Divisão por 0, operação inválida.'
    else: 
        resultado = 'Operador inválido.'
        
    lista_resultados.append(resultado)
    
print('------ Operações entre a Lista 1 e a Lista 2 -------')
print(lista_1)
print(lista_op)
print(lista_2)
print('----------------------------------------------------')
print(lista_resultados)
