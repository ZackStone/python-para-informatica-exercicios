# Exercício 9.4 Adicione linhas ao código anterior a fim de descobrir quem tem
# mais mensagens no arquivo.
# Após todos os dados serem lidos e o dicionário ser criado, olhe no dicionário usando
# uma estrutura de repetição máxima (olhe a Seção 5.7.2), para descobrir quem tem mais
# mensagens e imprima quantas mensagens a pessoa tem.

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

maior = None
for c in count:
	if maior == None or count[c] > count[maior]: maior = c

print (maior + ' : ' + str(count[maior]) + ' emails enviados.')