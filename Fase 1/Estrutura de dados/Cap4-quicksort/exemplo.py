def quicksort(array):
    if len(array) < 2: #caso base
        return array
    else:
        pivo = array[0] #pivo escolhido, ponto de partida
        menores = [i for i in array[1:] if i <= pivo] #elementos menores ou iguais ao pivo
        maiores = [i for i in array[1:] if i > pivo] #elementos maiores que o pivo
        return quicksort(menores) + [pivo] + quicksort(maiores) #retorno da chamada recursiva onde dentro da lista de maiores eu escolho um pivo e faço a partição novamente assim como com os menores

print(quicksort([10, 5, 2, 3]))