# coding: utf-8

# Exercício 4.7 Reescreva o programa de notas do capítulo anterior usando uma função
# chamada computegrau que recebe uma pontuação como parâmetro e retorna um grau,
# sendo este último uma string.

from decimal import *
def computegrau(p):
    if p > 1: print('Pontuação Ruim')
    elif p >= Decimal('0.9'): return 'A'
    elif p >= Decimal('0.8'): return 'B'
    elif p >= Decimal('0.7'): return 'C'
    elif p >= Decimal('0.6'): return 'D'
    else: return 'F'
try:
    p = Decimal(input('Digite uma pontuação: '))
    print(computegrau(p))
except:
    print('Pontuação Ruim')
