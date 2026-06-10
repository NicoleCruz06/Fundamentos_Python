# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 15:17:08 2026

@author: nicole.cruz
"""
carros={"fusca":7,"gol":10,"uno":12.5,"versa": 9,"yaris":14.5}

lista_litros = []
lista_valor = []
lista_carros = list(carros.keys())
lista_consumo = list(carros.values())

def menor_consumo(lista_consumo,lista_carros):
  # Inicializa com o primeiro carro e seu consumo como o mais econômico
  maior_consumo_km_l = lista_consumo[0]
  carro_mais_economico = lista_carros[0]
  for i in range(len(lista_consumo)):
    # Se o consumo atual (Km/L) for maior, este é o carro mais econômico até agora
    if lista_consumo[i] > maior_consumo_km_l:
      maior_consumo_km_l = lista_consumo[i]
      carro_mais_economico = lista_carros[i]
  return f'O carro mais econômico é o {carro_mais_economico}'

def gasolina(lista_consumo,distancia,preco_litro):
  for consumo in lista_consumo:
    litros = (distancia/consumo)
    lista_litros.append(litros)
  for litros in lista_litros:
    valor = (litros*preco_litro)
    lista_valor.append(valor)
  return lista_litros, lista_valor

def relatorio(lista_carros,lista_consumo,lista_litros,lista_valor):
  print(f'Comparativo de Consumo de Combustível para viagem de {distancia} km')
  print('Carro    Km/L    Litros   Valor Total')
  for i in range(len(lista_carros)):
    print(f'{i+1}-{lista_carros[i]}    {lista_consumo[i]:.2f}   {lista_litros[i]:.2f}    -R${lista_valor[i]:.2f}')

distancia = float(input('Digite a distância da viagem em kilômetros:').replace(',','.'))
preco_litro = float(input('Digite o preço do litro de gasolina:').replace(',','.'))

gasolina(lista_consumo,distancia,preco_litro)
relatorio(lista_carros,lista_consumo,lista_litros,lista_valor)
print(menor_consumo(lista_consumo,lista_carros))
