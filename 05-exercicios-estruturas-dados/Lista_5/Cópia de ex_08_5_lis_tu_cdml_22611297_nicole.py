# -*- coding: utf-8 -*-
"""
Created on Fri May 22 10:58:10 2026

@author: nicole.cruz
"""

palavra = input('Digite uma palavra:')

comprimento = len(palavra)

palavra_invertida = ""

indice = comprimento - 1

while indice >= 0:

    palavra_invertida += palavra[indice]
    
    indice -= 1

print(f"A palavra invertida é: {palavra_invertida}")

    