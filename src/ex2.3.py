# coding: utf-8

# Exercício 2.3 Escreva um programa no qual o usuário digite o número de horas
# trabalhadas e o valor pago por hora e calcule o salário bruto.
from decimal import *
horasTrabalhadas = Decimal(input('Horas trabalhadas: '))
salarioHora = Decimal(input('Valor pago por hora: '))
salarioBruto = horasTrabalhadas * salarioHora
print('Salário bruto: ' + str(round(salarioBruto, 2)))
