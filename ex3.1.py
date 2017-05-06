# coding: utf-8

# Exercício 3.1 Reescreva seu cálculo de pagamento para dar ao empregado 
# 1,5 vezes o valor da hora para quem trabalhou acima de 40 horas.

from decimal import *
horasTrabalhadas = Decimal(input('Horas trabalhadas: '))
salarioHora = Decimal(input('Valor pago por hora: '))
if horasTrabalhadas > 40: salarioHora *= Decimal(1.5)
salarioBruto = horasTrabalhadas * salarioHora
print('Salário bruto: ' + str(round(salarioBruto, 2)))
