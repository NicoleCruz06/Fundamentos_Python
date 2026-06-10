# -*- coding: utf-8 -*-
"""
Created on Fri May 22 10:20:27 2026

@author: nicole.cruz
"""
soma = 0
contador = 0
lista_temp = []
lista_meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
lista_acima_med = []

for mes in lista_meses:
    temp_med = float(input(f'Digite a temperatura média referente ao mês de {mes}:').replace(',','.'))
    lista_temp.append(temp_med)
    soma += temp_med
    
media_ano = (soma)/12

print('------ Temperaturas médias ao longo dos meses ------')
for mes in lista_meses:
    print(f'A temperatura média referente ao mês de {mes} foi {lista_temp[contador]}°C.')
    contador += 1
    
print(f'A média de temperatura no ano foi {media_ano}°C.')

for temp in lista_temp:
    if temp > media_ano:
        lista_acima_med.append(temp)
        
print(f'{len(lista_acima_med)} temperaturas ficaram acima da média do ano.\n Elas ocorreram nos meses:')

for mes, temp in zip(lista_meses, lista_temp):
    if temp > media_ano:
        print(f'- {mes}: {temp}°C')
        
        