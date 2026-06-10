# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 15:17:26 2026

@author: nicole.cruz
"""
temp_med = {
    'Janeiro': 33.0,
    'Fevereiro': 30.0,
    'Março': 30.0,
    'Abril': 25.0,
    'Maio': 25.0,
    'Junho': 24.0,
    'Julho': 20.0,
    'Agosto': 27.0,
    'Setembro': 27.0,
    'Outubro': 30.0,
    'Novembro': 30.0,
    'Dezembro': 30.0}

lista_mes = list(temp_med.keys())
lista_temp = list(temp_med.values())
lista_acima_temp = []
lista_acima_mes = []

def media(lista_temp):
    soma = 0
    for temp in lista_temp:
        soma += temp

    return (soma/12)

media_anual = media(lista_temp)

def meses_acima(media_,lista_temp):
    for i in range(len(lista_temp)):
        if lista_temp[i] > media_anual:
            lista_acima_temp.append(lista_temp[i])
            lista_acima_mes.append(lista_mes[i])

    return lista_acima_temp,lista_acima_mes

meses_acima(media_anual,lista_temp)

def relatorio(lista_acima_temp,lista_acima_mes,media_anual):
    print(f'---------Temperaturas Acima da Média Anual de {media_anual:.2f}°---------')
    print(f'{'Mês':<15} {'Temperatura':>29}')
    for i in range(len(lista_acima_temp)):
        print(f'{i+1} - {lista_acima_mes[i]:<15} {lista_acima_temp[i]:>19.2f}°')

print(f'A média anual foi de {media_anual:.2f}°')
relatorio(lista_acima_temp,lista_acima_mes,media_anual)
