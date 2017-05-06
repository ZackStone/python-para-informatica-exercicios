# Exercício 10.1 Revise o programa anterior como segue: Leia e analise as linhas
# “From” e extraia os endereços de cada linha. Conte o número de mensagens de cada pessoa
# usando um dicionário.
# Após todos os dados terem sido lidos, imprima a pessoa com mais submissões
# (commits) através da criação de uma lista de tuplas (contador, e-mail) do dicionário e
# então ordena a lista em ordem decrescente e imprima a pessoa que tem mais submissões.

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


lista = []
for c in count:
	el = (count[c], c)
	lista.append(el)

lista.sort(reverse=True)

print(lista[0])