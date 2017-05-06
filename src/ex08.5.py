# Exercício 8.5 Escreva um programa que leia os dados de uma caixa de e-mail
# e quando encontrar a linha que começa com “From”, divida a linha em palavras usando
# a função split. Estamos interessados em quem mandou a mensagem, que é a segunda
# palavra na linha From.

import os
curpath = os.path.dirname(os.path.abspath(__file__))
filepath = curpath + '/../data/mbox-short.txt'
fhand = open(filepath)

i = 0
for line in fhand:
	if line.startswith('From:'):
		sender = line.split(' ')[1].replace('\n', '')
		i += 1
		print(sender)

print('Contagem: ' + str(i))