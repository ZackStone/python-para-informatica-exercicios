# Exercício 9.2 Escreva um programa que categorize cada mensagem de e-mail
# pelo dia da semana que a submissão foi feita. Para fazer isso, procure por linhas que
# começam com “From”, e então procure pela terceira palavra e assim continue executando
# o contador para cada um dos dias da semana. No fim do programa imprima o conteúdo
# de seu dicionário (a ordem não importa).

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
	k = palavras[2]
	if k in count: count[k] += 1
	else: count[k] = 1

print(count)