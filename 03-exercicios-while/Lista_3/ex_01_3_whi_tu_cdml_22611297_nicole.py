# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""
i = 1
med = 0
qtd = int(input('Digite de quantos números a sua média vai se tratar:'))
while i <= qtd:
    num = float(input('Insira um valor:').replace(',','.'))
    med += num
    i += 1
media = med/qtd
print('O valor da média desses números é:',media)   
    
