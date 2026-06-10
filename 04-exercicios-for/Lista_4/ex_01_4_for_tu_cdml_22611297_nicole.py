# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""
contador = 0
soma = 0
num = int(input('Digite um número:').replace('.',','))
for contador in range(num):
    soma += num
    num -= 1
    contador += 1
media = soma/contador
print('Soma total:',soma)
print('A média da soma desse número a todos os seus antecessores até 0 é:',media)
