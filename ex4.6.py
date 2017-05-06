# coding: utf-8

# Exercício 4.6 Reescreva o programa de computação de pagamento com um tempo e
# meio das horas extras e crie uma função chamada computepagamento que recebe dois
# parâmetros (o número de horas e o valor pago por hora).

from decimal import *
def computepagamento(horasTrabalhadas, salarioHora):
    if horasTrabalhadas > 40: salarioHora *= Decimal(1.5)
    return horasTrabalhadas * salarioHora
try:
    horasTrabalhadas = Decimal(input('Horas trabalhadas: '))
    salarioHora = Decimal(input('Valor pago por hora: '))
    salarioBruto = computepagamento(horasTrabalhadas, salarioHora)
    print('Salário bruto: ' + str(round(salarioBruto, 2)))
except:
    print('Erro! Por favor, digite uma entrada numérica.')
