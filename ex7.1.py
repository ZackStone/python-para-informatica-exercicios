# Exercício 7.1 Escreva um programa para ler um arquivo e imprimir o conteúdo do
# arquivo (linha por linha), com todos os caracteres em maiúsculos.

fhand = open('data/mbox-short.txt')
for line in fhand:
	print(line.upper())

