# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 08:46:14 2026

@author: nicole.cruz
"""
genero = input('Digite M para Mulher e H para Homem:').upper()
altura = float(input('Digite a sua altura em metros:').replace(',','.'))
peso_m = (62.1*altura)-44.7
peso_h = (72.7*altura)-58
if genero=='M':
  print('Seu peso ideal é: %.2f' %peso_m)
elif genero=='H':
  print('Seu peso ideal é: %.2f' %peso_h)
else:
  print('Erro, gênero não identificado')

