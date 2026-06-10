# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 08:46:35 2026

@author: nicole.cruz
"""

preco_compra = float(input('Insira o valor da compra do produto:').replace(',','.'))
preco_venda = float(input('Insira o valor da venda do produto:').replace(',','.'))
if preco_venda-preco_compra > 0:
    print('O comerciante teve lucro, com um preço de compra de R$ %.2f'%preco_compra,'e um preço de venda de R$ %.2f'%preco_venda)
elif preco_venda-preco_compra < 0:
    print('O comerciante teve prejuízo, com um preço de compra de R$ %.2f'%preco_compra,'e um preço de venda de R$ %.2f'%preco_venda)
else:
    print('O comerciante não obteve nem lucro nem prejuízo, com um preço de compra de R$ %.2f'%preco_compra,'e um preço de venda de R$ %.2f'%preco_venda)