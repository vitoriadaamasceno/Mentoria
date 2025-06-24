## Typescript

### O que é Typescript?

- È um superset para linguagem JS, Ou seja, adiciona funções ao JavaScript, como tipagem estática, interfaces, classes e outros recursos que ajudam a criar aplicações mais robustas e escaláveis.
- è compilado em JS ou seja não executamos TS.

### Vantagens do Typescript

- Confiabilidade nos tipos : 
  - O Typescript permite que você defina tipos para variáveis, parâmetros e retornos de funções, o que ajuda a evitar erros comuns de digitação e lógica. Isso torna o código mais fácil de entender e manter.

- Novas funcionalidades como por exxemplos interfaces.

- Verifica erro antes da execução,no desenvolvimento. Pois a IDE não permite

- Diminui quantidades de BUGS de forma mais explicita. Não é necessário adivinhar o que a função faz, pois ela já tem um tipo definido.


## Introdução ao Typescript

### Tipos de dados

Em TS definimos os tipos das variáveis , dos retorno das funções e das manipulações de dados. Isso ajuda a evitar erros comuns de digitação e lógica, tornando o código mais fácil de entender e manter.

#### Tipos primitivos

Todos inseridos com letras minusculas

- Number: numeros inteiros, float , negativos. Aceita apenasnumeros, e possibilita uso de metodos numericos

- String: textos

- Boolean: boleanos

Annotation é quando defininos o tipo do dado, e Inference é quando TS identifica e define o tipo de dado

#### Mais tipos


- Array : Conjuntos de valores em uma lista que só aceita o mesmo tipo. Um array de inteiros só devem ter inteiros

  Criando 

  const numeros: numbers[] = [1,2,3]


  Outra forma de criar

  const num: Array<number> = [1,2,3]

- Any: aceita qualquer tipo, deve ser evitado.

- Definindo o tipo nos parametros: passar a tipagem de um parametro para evitar erro

  function soma(a:number,b:number){
    console.log(a+b)
  }

- Assim como podemos tipar o retorno. Definindo o tipo do resultado

  function soma(a:number, b:number): number {
    return a+b
  }

- Union type : pode juntar mais tipos para serem aceitos

- Alias : permite criar um tipo e determinar o que ele verifica

- Interfaces: uma outra maneira de nomear e tipar um objeto. Escolhendo suas propriedades e seus tipo.

  A diferença entre type e interface, são bastente parecidas e podemos optar por um outro porém a Interface pode ser alterada ao longo do código já o type não.

- Literal types : estilo um enum onde definimos os valores aserem recebidos.

- Non-null : usar o caractere ! para valores que ainda vão ser preenchidos