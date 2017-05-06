# Exercício 7.2 Escreva um programa para perguntar por um nome de arquivo, e
# então, ler o arquivo e procurar por linhas da forma:
# X-DSPAM-Confidence: 0.8475
# Quando você encontra uma linha que começa com “X-DSPAM-Confidence:” separe
# a linha para extrair dela o número com ponto flutuante. Conte essas linhas e determine
# o valor total médio dos valores de confiança de spam a partir destas linhas.
# Quando você alcançar o fim do arquivo, imprima a confiança média de spam.
# Teste seu programa sobre os arquivos mbox.txt e mbox-short.txt.

fhand = None
while fhand == None:
	filename = input('Nome do arquivo: ')
	try:
		fhand = open('data/' + filename)
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