## Ordenação por Seleção

- A memoria do seu computador é como um conjunto gigante de gavetas.
- Quando se quer armazenar multiplos elementos , usa-se array ou listas
- No array, todos os elementos são armazenados um do lado do outro.
- Na lista, os elementos estão espalhados e um elemento armazena o endereço do proximo elemento.
- Arrays permitem leituras rápidas.
- Listas encadeadas permitem rápidas inserções e eliminações.
- Todos os elementos de um array devem ser do mesmo tipo (todos ints, todos os doubles, e assim por diante)



### Tempo de execução : Array x Listas encadeadas

| Operação  | Arrays | Listas |
|----------|--------|--------|
| Leitura  | O(1)   | O(n)   |
| Inserção | O(n)   | O(1)   |
| Deletar  | O(n)   | O(1)   |


Ou seja, arrays são melhores para leitura porém as listas performam melhor para inserção e deleção. Considerando a alocação de memória.
