# Exercício 7.3 Às vezes quando programadores se chateiam ou querem ter um
# mínimo de diversão, eles adicionam um Ovo de Páscoa inofensivo aos seus programas
# Modifique o programa que pergunta ao usuário um nome de arquivo e então 
# imprime uma mensagem engraçada quando o usuário digita o nome de arquivo “na na boo boo”.
# O programa deve se comportar normalmente para todos os outros arquivos que existem ou 
# que não existem.

import os
curpath = os.path.dirname(os.path.abspath(__file__))
filepath = curpath + '/../data/'

fhand = None
while fhand == None:
	filename = input('Nome do arquivo: ')
	if filename == 'na na boo boo':
		print('NA NA BOO BOO TO YOU! you have been punk\'d')
	else:
		try:
			fhand = open(filepath + filename)
		except:
			print('Arquivo não encontrado.')

fa = []
for line in fhand:
	if line.startswith('X-DSPAM-Confidence: '):
		pos = line.find(':') + 2
		f = float(line[pos:])
		fa.append(f)

media = sum(fa) / len(fa)
print('Average spam confidence: ' + str(round(media, 3)))