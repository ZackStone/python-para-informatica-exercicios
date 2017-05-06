# Exercício 9.5 Escreva um programa que registre o nome de domínio 
# (ao invés do endereço) de onde a mensagem foi enviada ao invés de
# onde o e-mail veio (ou seja, o endereço de e-mail inteiro).
# No final do programa imprima os conteúdos do dicionário.

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
	k = palavras[1].split('@')[1]
	if k in count: count[k] += 1
	else: count[k] = 1

maior = None
for c in count:
	if maior == None or count[c] > count[maior]: maior = c

print (maior + ' : ' + str(count[maior]) + ' emails enviados.')
print(count)