#lista = int(input('Digite vasrios numeros: '))
lista = [10, 4, 7, 8, 2, 5, 19]
lista1 = sorted(lista)
lista.sort()
lista2 = lista
print('lista 1 {}'.format(lista1))
print('lista 2 {}'.format(lista2))

lit = lista
if lit[0] > lit[1]:
    aux = lit[1]
    lit[1] = lit[0]
    lit[0] = aux
print('Outra forma de ordenação: {}'.format(lit))
