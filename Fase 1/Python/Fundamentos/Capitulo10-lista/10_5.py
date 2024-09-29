def is_sorted(lista):
    if sorted(lista) == lista:
        return True
    else: 
        return False
    
    

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(is_sorted(lista))
