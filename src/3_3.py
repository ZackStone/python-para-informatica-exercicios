# coding: utf-8

# Exercício 3.3 Escreva um programa que solicite um valor entre 0.0 e 1.0. Se o
# valor está fora do intervalo imprima um erro. Se o valor está entre 0.0 e 1.0, 
# imprima um conceito de acordo com a tabela a seguir:

from decimal import *
try:
    p = Decimal(input('Digite uma pontuação: '))
    if p >= Decimal('0.9'): print('A')
    elif p >= Decimal('0.8'): print('B')
    elif p >= Decimal('0.7'): print('C')
    elif p >= Decimal('0.6'): print('D')
    else: print('F')
except:
    print('Pontuação Ruim')
