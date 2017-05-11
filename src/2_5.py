# coding: utf-8

# Exercício 2.5 Escreva um programa que toma como entrada uma temperatura
# em Celsius, converta-a em Fahrenheit e imprima a temperatura convertida.

from decimal import *
celsius = Decimal(input('Temperatura em Celsius: '))
f = celsius * 9/5 + 32
print('Temperatura em Fahrenheit: ' + str(f))
