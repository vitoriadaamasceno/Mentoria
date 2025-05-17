def busca_simples(lista, elemento):
    """
    Busca um elemento em uma lista e retorna o índice do elemento se encontrado, ou -1 se não encontrado.
    

    :return: Índice do elemento na lista ou -1 se não encontrado
    """
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

lista = [1, 2, 3, 4, 5]
elemento = 3
indice = busca_simples(lista, elemento)
print(indice)