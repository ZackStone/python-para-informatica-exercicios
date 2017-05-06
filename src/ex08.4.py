# Exercício 8.4 Faça o download do arquivo de www.py4inf.com/code/romeo.txt
# Escreva um programa que abra o arquivo romeo.txt e leia-o linha por linha. Para
# cada linha, separe-a em uma lista de palavras usando a função split.
# Para cada palavra, cheque para ver se a palavra já está em uma lista.
# Se não estiver na lista, adicione-a.
# Quando o programa estiver completo, organize e imprima as seguintes palavras
# em ordem alfabética.

import os
curpath = os.path.dirname(os.path.abspath(__file__))
filepath = curpath + '/../data/romeo.txt'
fhand = open(filepath)

vet = []
for line in fhand:
	vet2 = line.split(' ')
	for v in vet2:
		v = v.replace('\n', '')
		if v not in vet:
			vet.append(v)

vet.sort()
print(vet)