# Exercício 9.1 Escreva um programa que leia palavras em words.txt e as 
# armazene como chaves em um dicionário. Não importa o que os valores são.
# Então você pode usar o operador in como um meio rápido de verificar 
# se uma string está no dicionário.

import os
curpath = os.path.dirname(os.path.abspath(__file__))
fhand = open(curpath + '/../data/words.txt')
d = dict()
for l in fhand:
	for w in l.split(' '):
		w = w.replace('\n', ' ')
		if w not in d:
			d[w] = None

print(d)

