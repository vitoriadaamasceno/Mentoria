def pesquisa_binaria(lista, item):
    '''
    Pesquisa binária de um elemento em uma lista ordenada.
    :param lista: Lista ordenada onde o elemento será buscado
    :param item: Elemento a ser buscado
    :return: Índice do elemento na lista ou None se não encontrado
    '''
    menor = 0
    maior = len(lista) - 1

    while menor <= maior:
        meio = int((menor+maior)/2)
        chute = lista [meio]
        
        if chute == item :
            return meio
        if chute > item:
            maior = meio - 1
        else:
            menor = meio + 1
    return None

lista = [1,2,3,4,5]
print(pesquisa_binaria(lista,5))