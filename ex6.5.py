# coding: utf-8

# Exercicio 6.5: Use o método find e fragmente a string para extrair a porção 
# da string depois dos dois pontos e então use a função float para converter 
# a string extraída em um número com ponto flutuante.

str = 'X-DSPAM-Confidence: 0.8475'
pos = str.find(':') + 2
f = float(str[pos:])
print(f)
