# Exercício 8.2 Descubra qual linha do programa anterior ainda não está guardada
# propriamente. Tente construir um caso de teste que faça o programa falhar e o
# modifique para que a linha esteja guardada apropriadamente e teste para ter certeza
# de que ele seja capaz de avaliar seu novo caso de teste.

#
# Não entendi
#

import os
curpath = os.path.dirname(os.path.abspath(__file__))
filepath = curpath + '/../data/'

fhand = open(filepath + 'mbox-short.txt')
count = 0
for line in fhand:
	palavras = line.split()
	#print('Debug: ', palavras)
	if len(palavras) == 0 : continue
	if palavras[0] != 'From' : continue
	print (palavras[2])