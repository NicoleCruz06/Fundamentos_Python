# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 15:15:52 2026

@author: nicole.cruz
"""
import math
def potencia(x,y):
    return(x**y)

def hipotenusa(b,c):
  b_2 = potencia(b,2)
  c_2 = potencia(c,2)
  return math.sqrt(b_2 + c_2)

b = int(input('Digite o valor do cateto adjacente:'))
c = int(input('Digite o valor do cateto oposto:'))

print(f'O valor da hipotenusa de um triângulo com um cateto adjacente equivalente a {b} e um cateto oposto {c} é {hipotenusa(b,c)}. ')

