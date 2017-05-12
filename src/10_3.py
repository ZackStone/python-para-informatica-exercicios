# Exercício 10.3 Escreva um programa que leia um arquivo e imprima as letras
# em ordem decrescente de frequência. Seu programa deve converter todas as entrada para
# minúsculo e somente contar as letras de a-z. Seu programa não deve contar espaços, dígitos,
# pontuação ou qualquer outros que não sejam as letras de a-z. Encontre exemplos de textos
# de diferentes linguagens e veja como a frequência das letras variam entre as linguagens.
# Compare seu resultado com as tabelas em wikipedia.org/wiki/Letter_frequencies.

import os

def conta(arquivo):

	curpath = os.path.dirname(os.path.abspath(__file__))
	filepath = curpath + '/../data/'

	fhand = open(filepath + arquivo)

	count = dict()
	for line in fhand:
		letras = list(line)
		for letra in letras:
			letra = letra.lower()
			if letra >= 'a' and letra <= 'z':
				if letra in count: count[letra] += 1
				else: count[letra] = 1


	lista = []
	for c in count:
		el = (count[c], c)
		lista.append(el)

	lista.sort(reverse=True)


	soma = 0
	for l in lista:
		soma += l[0]

	i = 1
	for l in lista:
		if i > 5: break
		p = round(l[0] / soma * 100, 2)
		print('  ' + l[1] + ' ' + str(p) + ' %')
		i += 1

print('Inglês')
arquivo = 'bor-stat.txt'
conta(arquivo);

print('Alemão')
arquivo = 'german.txt'
conta(arquivo);

print('Espanhol')
arquivo = 'spanish.txt'
conta(arquivo);

print('Francês')
arquivo = 'fr.txt'
conta(arquivo);

print('Português')
arquivo = 'pt.txt'
conta(arquivo);