def buscaMenor(arr):
    menor = arr[0]
    menor_index = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_index = i
    return menor_index
def ordenacao_selecao(arr):
    novo_arr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novo_arr.append(arr.pop(menor))
    return novo_arr

# Testando a função de ordenação por seleção
arr = [5, 3, 6, 2, 10]
arr_ordenado = ordenacao_selecao(arr)
print(arr_ordenado)
        
resultado='10'
resultado = resultado
print(resultado)