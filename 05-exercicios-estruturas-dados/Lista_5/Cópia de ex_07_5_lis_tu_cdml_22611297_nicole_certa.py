# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""
frase = str(input('Digite uma frase:'))

vogais = set('aáàãâeéêiíoóôõuúü')

lista_consoantes = [
    letra for letra in frase.lower()
        if letra.isalpha() and letra not in vogais
    ]

print(f'Há {len(lista_consoantes)} consoantes na frase digitada.')
print(f'As consoantes digitadas na frase são {lista_consoantes}.')
