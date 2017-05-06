# Exercício 9.3 Escreva um programa que leia um log de e-mails e construa um
# histograma usando um dicionário para contar quantas mensagens vem de cada endereço
# de e-mail. Imprima o dicionário.

import os
curpath = os.path.dirname(os.path.abspath(__file__))
filepath = curpath + '/../data/'
fhand = open(filepath + 'mbox.txt')

count = dict()
for line in fhand:
	palavras = line.split()
	#print('Debug: ', palavras)
	if len(palavras) == 0 : continue
	if palavras[0] != 'From' : continue
	k = palavras[1]
	if k in count: count[k] += 1
	else: count[k] = 1

print(count)