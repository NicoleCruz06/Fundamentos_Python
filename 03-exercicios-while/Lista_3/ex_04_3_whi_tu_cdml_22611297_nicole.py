# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 08:35:34 2026

@author: nicole.cruz
"""
aluno = 1
med = 0
while aluno <= 50:
    print('Insira o valor da nota do aluno', aluno,':')
    nota = float(input().replace(',','.'))
    aluno += 1 
    med += nota
media = med/50
print('A média da turma é: %.2f'%media)

    
    
