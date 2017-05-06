# coding: utf-8

# Exercício 3.2 Reescreva seu programa de pagamento usando try e except tal
# que seu programa trate a entrada não numérica, imprimindo uma mensagem e finalizando
# a execução do mesmo neste caso. O trecho a seguir mostra duas execuções do programa:

from decimal import *
try:
    horasTrabalhadas = Decimal(input('Horas trabalhadas: '))
    salarioHora = Decimal(input('Valor pago por hora: '))
    if horasTrabalhadas > 40: salarioHora *= Decimal(1.5)
    salarioBruto = horasTrabalhadas * salarioHora
    print('Salário bruto: ' + str(round(salarioBruto, 2)))
except:
    print('Erro! Por favor, digite uma entrada numérica.')
