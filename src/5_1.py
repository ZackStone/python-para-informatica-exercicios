# coding: utf-8

# Exercício 5.1 Escreva um programa que leia números repetidamente até que o
# usuário informe “done”. Uma vez que “done” é informado, imprima a soma, quantidade
# e média dos números. Se o usuário digita alguma coisa diferente de um número, detecte
# o erro usando try e except e imprima uma mensagem de erro e pule para o próximo número.

n = []
while True:
    i = input('Digita aí: ')
    if i == 'done': break
    try:
        n.append(int(i))
    except:
        print('Invalid input')
    
print('Soma: ' + str(sum(n)))
print('Média: ' + str(sum(n) / len(n)))
