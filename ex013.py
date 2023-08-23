def executar_bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n-1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
lista = [55, 34, 65, 8, 7, 2, 89, 44, 44]
res = executar_bubble_sort(lista)
print('Resultado é {}'.format(res))
