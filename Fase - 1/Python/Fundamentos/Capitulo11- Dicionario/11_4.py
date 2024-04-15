def has_duplicates(lista):
    return len(lista) != len(set(lista))


d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 6, 'f': 6, 'g': 7, 'h': 8, 'i': 9}
def has_duplicates2(d):
    return len(d) != len(set(d[i] for i in d.keys( )))

print(has_duplicates2(d))