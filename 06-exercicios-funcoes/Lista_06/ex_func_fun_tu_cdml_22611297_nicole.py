# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 15:17:43 2026

@author: nicole.cruz
"""
funcionarios_gulosos= {
    'Alexandre': 456123789,
    'Anderson': 1245698456,
    'Antonio': 123456456,
    'Carlos': 91257581,
    'Cesar': 987458,
    'Rosemary': 789456125}

lista_pct = []
lista_megabytes = []
lista_func = list(funcionarios_gulosos.keys())
lista_espaco = list(funcionarios_gulosos.values())

def megabyte(lista_espaco):
    for tamanho in lista_espaco:
        tamanho = tamanho / (1024* 1024)
        lista_megabytes.append(tamanho)
    return

megabyte(lista_espaco)

def total(lista_megabytes):
    soma = 0
    for espaco in lista_megabytes:
        soma += espaco
    return soma

def media(lista_megabytes):
    return (total(lista_megabytes)/(len(lista_megabytes)))

def porcentagem(lista_megabytes):
    for i in range(len(lista_megabytes)):
        pct = (lista_megabytes[i]/total(lista_megabytes))*100
        lista_pct.append(pct)
    return lista_pct

porcentagem(lista_megabytes)

def menor_espaco(lista_megabytes):
    menor = lista_megabytes[0]
    menor_func = lista_func[0] # Renomeado para evitar confusão com variável global não atribuída
    for i in range(len(lista_megabytes)):
        if lista_megabytes[i] < menor:
            menor = lista_megabytes[i]
            menor_func = lista_func[i]
    return menor_func

def maior_espaco(lista_megabytes):
    maior = lista_megabytes[0]
    maior_func = lista_func[0] # Renomeado para evitar confusão com variável global não atribuída
    for i in range(len(lista_megabytes)):
        if lista_megabytes[i] > maior:
            maior = lista_megabytes[i]
            maior_func = lista_func[i]
    return maior_func

menor_espaco(lista_megabytes)
maior_espaco(lista_megabytes)

def relatorio(lista_func,lista_megabytes,lista_pct):
    print('ACME Inc.       Uso do espaço em disco pelos usuários')
    print('-' * 55 )
    print('Nr. Usuário    Espaço utilizado    % do uso\n')
    for i in range(len(lista_func)):
        print(f'{i+1} - {lista_func[i]:<8} {lista_megabytes[i]:>10.2f} {lista_pct[i]:>15.2f}')

relatorio(lista_func,lista_megabytes,lista_pct)
print(f'\nEspaço total ocupado: {total(lista_megabytes):.2f} MB')
print(f'Espaço médio ocupado: {media(lista_megabytes):.2f} MB')
print(f'Maior consumo de espaço: {maior_espaco(lista_megabytes)}')
print(f'Menor consumo de espaço: {menor_espaco(lista_megabytes)}')
