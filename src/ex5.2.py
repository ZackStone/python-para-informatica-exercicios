# coding: utf-8

# Exercício 5.2 Escreva um programa que pede por uma lista de números e imprima
# o maior e o menor dos números. Sua entrada deve respeitar as condições impostas no
# Exercício 5.1.

n = []
while True:
    i = input('Digita aí: ')
    if i == 'done': break
    try:
        n.append(int(i))
    except:
        print('Tenta de novo')
    
print('Max: ' + str(max(n)))
print('Min: ' + str(min(n)))
