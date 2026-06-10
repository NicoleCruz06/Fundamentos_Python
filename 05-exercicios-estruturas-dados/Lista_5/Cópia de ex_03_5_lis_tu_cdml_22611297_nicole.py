# -*- coding: utf-8 -*-
"""
Created on Fri May 22 11:22:14 2026

@author: nicole.cruz
"""

lista_notas = []
lista_alunos = [1,2,3,4,5,6,7,8,9,10]
soma = 0
acima_media = 0
for contador in range(10):
  nota = float(input(f'Digite a nota do aluno {contador+1}:').replace(',','.'))
  if nota > 10 or nota < 0:
    print('Nota inválida. Por favor insira um valor entre 0 e 10.')
    continue
  lista_notas.append(nota)
  soma += nota
media = (soma)/10
for nota in lista_notas:
  if nota > media:
    acima_media += 1

print('------ Relátorio de notas da turma ------')
print('Notas: ',lista_notas,'\nAlunos:',lista_alunos)
print('Média: %.2f'%media)
print('Notas acima da média: ',acima_media)