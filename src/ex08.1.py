# Exercício 8.1 Escreva uma função chamada chop que receba uma lista e a 
# modifique, removendo o primeiro e o último elemento, e retorne None.
# Em seguida, escreva uma função chamada middle que receba uma lista e 
# retorne uma nova lista que contem todos exceto o primeiro e o último elemento.

def chop(lista):
	del lista[0]
	del lista[len(lista)-1]
	return None

def middle(lista):
	return lista[1:-1]

lista = [1,2,3,4,5]
print('lista: ' + str(lista))
print('middle(lista): ' + str(middle(lista)))
print('lista: ' + str(lista))
print('chop(lista): ' + str(chop(lista)))
print('lista: ' + str(lista))
