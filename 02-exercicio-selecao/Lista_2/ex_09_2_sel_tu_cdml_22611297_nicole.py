# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 08:47:23 2026

@author: nicole.cruz
"""

import math
a = float(input('Insira o valor do coeficiente angular:'))
b = float(input('Insira o valor do coeficiente linear:'))
c = float(input('Insira o valor do termo independente:'))
delta = (b**2)-(4*a*c)
x1 = (-b + math.sqrt(delta))/(2*a)
x2 = (-b - math.sqrt(delta))/(2*a)
if delta > 0:
  print('A equação possui duas raízes reais diferentes, sendo elas:',x1,',',x2)
elif delta == 0:
  print('A equação possui duas raízes reais iguais, sendo ela:',x1)
elif delta < 0:
  print('A equação não possui raízes reais')
else:
  print('Erro')

      