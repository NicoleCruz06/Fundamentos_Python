# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""

ano_de_nasc = int(input('Digite o ano de seu nascimento:'))
idade = 2026-ano_de_nasc
if idade >= 16:
    print('A idade é',idade,'anos, visto que nasceu em',ano_de_nasc,', e já pode votar')
else:
    print('A idade é',idade,'anos, visto que nasceu em',ano_de_nasc,', e não pode votar')
