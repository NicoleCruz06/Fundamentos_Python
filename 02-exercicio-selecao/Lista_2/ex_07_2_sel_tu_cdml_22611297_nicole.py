# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 08:47:00 2026

@author: nicole.cruz
"""

nota1 = float(input('Insira o valor da primeira nota:').replace(',','.'))
peso1 = float(input('Insira o valor do peso da primeira prova:').replace(',','.'))
nota2 = float(input('Insira o valor da segunda nota:').replace(',','.'))
peso2 = float(input('Insira o valor do peso da segunda prova:').replace(',','.'))
media = (nota1*peso1 + nota2*peso2)/(peso1 + peso2)
if media >= 5:
    print('A média do aluno foi: %.2f'%media,'.Aluno aprovado')
else:
    print('A média do aluno foi: %.2f'%media,'.Aluno reprovado')