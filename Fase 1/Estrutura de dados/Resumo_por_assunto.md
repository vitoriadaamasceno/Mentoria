
# Resumo de Algoritmos – *Entendendo Algoritmos*

## 🔍 Pesquisa Simples

**Conceito**  
A *pesquisa simples* percorre todos os elementos de uma lista até encontrar o valor desejado. É ineficiente em listas grandes.

**Complexidade**: `O(n)`

**Exemplo**
```python
def pesquisa_simples(lista, item):
    for i in range(len(lista)):
        if lista[i] == item:
            return i
    return None

print(pesquisa_simples([10, 20, 30, 40], 30))  # Saída: 2
```

---

## 🔎 Pesquisa Binária

**Conceito**  
Funciona apenas em *listas ordenadas*. Divide a lista ao meio repetidamente, descartando metade a cada passo.

**Complexidade**: `O(log n)`

**Exemplo**
```python
def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1

    return None

print(pesquisa_binaria([1, 3, 5, 7, 9], 3))  # Saída: 1
```

---

## 📈 Notação Big O

**Conceito**  
Descreve *a eficiência de um algoritmo* em termos de tempo ou espaço, considerando o *pior caso*.

**Tabela de Complexidades**

| Nome           | Big O     | Exemplo                       |
|----------------|-----------|-------------------------------|
| Constante      | `O(1)`    | Acesso direto a um índice     |
| Logarítmica    | `O(log n)`| Pesquisa binária              |
| Linear         | `O(n)`    | Pesquisa simples              |
| Quadrática     | `O(n²)`   | Ordenação por seleção         |

---

## 📊 Ordenação por Seleção

**Conceito**  
Encontra o menor elemento da lista e o coloca na primeira posição. Repete isso até a lista estar ordenada.

**Complexidade**: `O(n²)`

**Exemplo**
```python
def menor(lista):
    menor_valor = lista[0]
    menor_indice = 0
    for i in range(1, len(lista)):
        if lista[i] < menor_valor:
            menor_valor = lista[i]
            menor_indice = i
    return menor_indice

def ordenacao_por_selecao(lista):
    nova_lista = []
    for i in range(len(lista)):
        menor_ind = menor(lista)
        nova_lista.append(lista.pop(menor_ind))
    return nova_lista

print(ordenacao_por_selecao([5, 3, 6, 2, 10]))  # Saída: [2, 3, 5, 6, 10]
```

---

## 📦 Arrays e Listas Encadeadas

**Arrays**
- Acesso rápido a um elemento via índice (`O(1)`).
- Inserção/remoção é lenta (`O(n)`).

**Listas Encadeadas**
- Inserção/remoção eficiente (`O(1)` se tiver ponteiro).
- Acesso lento aos elementos (`O(n)`).

**Exemplo (conceitual)**

```
Array:             [10, 20, 30]
Lista Encadeada:   10 → 20 → 30
```

---

## 🔁 Recursão

**Conceito**  
Uma função que chama a si mesma para resolver subproblemas.

**Exemplo: Fatorial**
```python
def fatorial(n):
    if n == 1:
        return 1
    return n * fatorial(n - 1)

print(fatorial(5))  # Saída: 120
```

---

## ⚡ Quicksort

**Conceito**  
Algoritmo de ordenação eficiente que usa recursão e a ideia de “pivô”.O quicksort adota a estratégia de **divisão e conquista**. A estratégia consiste em rearranjar de modo que os números maiores fiquem a direita do pivô e os números menores a esquerda, fazendo isso de forma recursiva, assim a lista fica cada vez menor.

**Complexidade**
- Média: `O(n * log n)`
- Pior caso: `O(n²)`

**Exemplo**
```python
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivo = array[0]
        menores = [i for i in array[1:] if i <= pivo]
        maiores = [i for i in array[1:] if i > pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)

print(quicksort([10, 5, 2, 3]))  # Saída: [2, 3, 5, 10]
```
