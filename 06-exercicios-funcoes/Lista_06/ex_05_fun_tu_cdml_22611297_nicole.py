# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 15:16:50 2026

@author: nicole.cruz
"""
def quantidade(num):
  return f'O número {num} possui {len(str(num))} digitos.'

num = int(input('Digite um número inteiro:'))

print(quantidade(num))


