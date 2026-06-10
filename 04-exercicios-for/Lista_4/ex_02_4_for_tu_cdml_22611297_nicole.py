# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""
soma = 0
print('Números entre 30 e 5 divisíveis por 3')
for contador in range(30,4,-1):
    if contador % 3 == 0:
        print(contador)
        soma += contador
print('A soma desses números é:',soma)
