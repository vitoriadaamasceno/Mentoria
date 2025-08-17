'''

🧩 Problema
Você recebeu uma lista com as notas finais dos alunos em uma disciplina. Sua tarefa é:

Implementar a ordenação por seleção para ordenar os valores.

Imprimir a lista ordenada em ordem crescente.
'''

def menor(lista):
    menor_valor = lista[0] #um possivel menor valr
    menor_indice = 0 #o indice do menor numero incialmente
    for i in range(1, len(lista)):
        if lista[i] < menor_valor:
            menor_valor = lista[i]
            menor_indice = i

    return menor_indice


def ordenacao_selecao(lista):
    new_lista = []
    for i in range(len(lista)):
        menor_ind = menor(lista)
        new_lista.append(lista.pop(menor_ind))
    return new_lista


notas = [8.5, 7.0, 9.3, 6.8]
print(ordenacao_selecao(notas))
