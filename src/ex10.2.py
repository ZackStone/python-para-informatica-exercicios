# Exercício 10.2 Este programa deve contar a distribuição das horas por dia para
# cada uma das mensagens. Você pode extrair a hora da linha “From” por encontrar a string
# de tempo e então dividí-la em partes usando o caracter dois pontos (:). Uma vez que você
# acumulou o contador para cada hora, imprima o contador, um por linha, ordenado pelas
# horas, como mostrado abaixo.

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
	dp = line.find(':')
	hora = line[dp-2:dp]
	if hora in count: count[hora] += 1
	else: count[hora] = 1


lista = []
for c in count:
	el = (c, count[c])
	lista.append(el)

lista.sort()

for i in lista:
	print(i)