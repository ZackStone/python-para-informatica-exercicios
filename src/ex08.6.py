# Exercício 8.6 Reescreva o programa que pede ao usuário uma lista de números e
# imprime o maior e o menor dos números lidos. A leitura deve terminar quando o usuário
# digitar “pronto”. Escreva o programa para armazenar os números que o usuário digita em
# uma lista e use as funções max() e min() para calcular o maior e o menor número quando
# a estrutura de repetição da leitura terminar.

n = []
while True:
    i = input('Digita aí: ')
    if i == 'pronto': break
    try:
        n.append(int(i))
    except:
        print('Tenta de novo')
    
print('Max: ' + str(max(n)))
print('Min: ' + str(min(n)))