# Exercício 7.1 Escreva um programa para ler um arquivo e imprimir o conteúdo do
# arquivo (linha por linha), com todos os caracteres em maiúsculos.

import os
curpath = os.path.dirname(os.path.abspath(__file__))
filepath = curpath + '/../data/mbox-short.txt'
fhand = open(filepath)
for line in fhand:
	print(line.upper())

