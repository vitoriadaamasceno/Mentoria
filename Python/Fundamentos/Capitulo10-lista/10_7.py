
lista = [1, 2, 3, 4, 6, 6, 7, 8, 9]

def has_duplicates(lista):
    return len(lista) != len(set(lista))

a=has_duplicates(lista)
print(a)