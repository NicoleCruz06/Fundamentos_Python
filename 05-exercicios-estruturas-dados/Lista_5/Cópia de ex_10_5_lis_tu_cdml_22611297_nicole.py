# -*- coding: utf-8 -*-
"""
Created on Fri May 22 10:57:50 2026

@author: nicole.cruz
"""
lista_alturas = []
lista_idades = []
soma = 0

for contador in range(30):
    idade = int(input(f'Digite a idade do aluno {contador+1}:'))
    altura = float(input(f'Digite a altura do aluno {contador+1}:').replace(',','.'))
    lista_alturas.append(altura)
    lista_idades.append(idade)
    soma += altura
    
media = soma/30
print(f'A média de altura dos alunos é {media}.')
 
for posicao, (idade, altura) in enumerate(zip(lista_idades, lista_alturas)):
    if idade > 13 and altura > media:
        print(f'O aluno {posicao + 1} tem {idade} anos e mede {altura}m (acima da média).')