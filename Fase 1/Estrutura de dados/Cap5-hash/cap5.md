## Tabela Hash (ou Tabela de Dispersão):


A tabela hash consiste em um algoritmo O(1), onde é uma função na qual você insere uma string e depois retorna um numero. Cada item adicionado é relacionado a um index e um valor relacionado. Um exemplo de hash é os dicts do python e os objects em js.

- Uma estrutura de dados especializada para armazenar dados em pares chave-valor, com o objetivo de permitir operações de busca, inserção e remoção muito rápidas (em tempo constante em alguns casos). 
- Utiliza uma função de dispersão (hash) para mapear uma chave para um índice na tabela, onde o valor correspondente é armazenado. 
- A função hash mapeia strings e números;
- A função hash não permite duplicatas;
- A tabela hash não armazena direto na memória diferente das listas e arrays que mapeiam direto para memória, os hash indica para onde armazenar esse dado;

### Utilidade

As tabelas hash são utéis para:

- Modelar relações entre dois itens
- Filtrar duplicatas 
- Caching/memorização de dados, em vez de solicitar estes dados do servidor.



#### Colisão


#### Desempenho