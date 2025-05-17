def fatorial(numero):
    if numero < 2:
        return 1
    return numero * fatorial(numero - 1)


#uso 
#print(fatorial(998))


def inverte_lista(lista):
    if not lista: #verifica se lista está vazia 
        return lista
    ultimo = lista[-1:]
    lista_resultado = ultimo + inverte_lista(lista[:-1]) #pega a última posição da lista e concatena com o resultado da chamada recursiva que inverte a lista menos o último elemento
    return lista_resultado


#testando
#print(inverte_lista([1,2,3,4,5]))



