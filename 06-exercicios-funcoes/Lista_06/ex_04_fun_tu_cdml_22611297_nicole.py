# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 15:16:44 2026

@author: nicole.cruz
"""
def inteiro(num):
  if num > 0:
    return f'O número {num} é positivo.'
  elif num < 0:
    return f'O número {num} é negativo.'
  else:
    return f'O número {num} é nulo.'

num = int(input('Digite um número inteiro:'))

print(inteiro(num))