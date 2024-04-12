def chop(lista):
    del lista[0]
    del lista[-1]
    return None

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(chop(lista))
print(lista)