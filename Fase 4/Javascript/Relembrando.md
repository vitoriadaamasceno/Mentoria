## Relembrando coisas importantes

### ECMAScript

É uma nova versão com recursos do javascript, cada vez ela vai se atualizando com mudanças no javascript o mais atual é o ECM15 lançada em 2024.

### Váriaveis 

#### Tipos de varivavés

Os tipos podem ser 
- Number(inteiros, float, negativos)
- Special Number(Infinity, Nan[not number], -Infinity )
    - exemplo ao tentar fazer isso console.log(12*"abc") -> o resultado é Nan , em python ele iria multiplicar a string
- String( textos com aspas duplas , simples ou crase)
- Boleanos(true, false - em minusculo, sinais >,>,==)
    - Comparação:
        Maior e menor que <>
        Igual ==
        diferente !==
        idêntico ===
- Operadores Lógicos (&& , ||, !)

- Empty Values ( undefined e null):
     - undefined usado ao utilizar algo no código que ainda não foi definido | é undefined
     - Null determinado por quem escreve para dizer que ainda não há valor | è um Object


Dicas: usar typeof() para descobrir o tipo

Dicas : Js acaba mudando o valor das coisas sozinho,temos que tomar cuidado
    Exemplo:
        
        - 5*null = 0
        
        - "5" - 3 = 2
        
        - "5" + 1 = 51
        
        - "a"* "b" = NaN

#### Declaração
- Constantes(const): Serve para salvar dados que não podem alterados. Ou seja só podemos declarar o valor de uma constante uma vez. Não sendo permitido transforma-la durante seu código

    Exemplo: 
    ```
    const nome = 'Vitoria'
    
    ```

- Varivavel(var): Serve para salvar dados que podem ser alterados. Geralmente usado para escopos globais e local em casos que os valores podem mudar.

    Exemplo: 
    ```
    var nome = 'Vitoria'
    nome = 'Maria Vitoria'
    
    ```

- Variavel(let): Foi uma tipo de variavel criado no ecma6. Usado no escopo global, local e de bloco(qualquer contexto entre {}, essa variavel com let só vai existir dentro desse bloco, já com var ele pode ser acessado).


### Funções e parâmetros

- Como é uma função em js: Geralmente criada com a palavra function , nome, parametros entre() , e o corpo dentro de um bloco{}. Toda função deve retornar um valor. Funções tem escopo global, ou seja, qualquer variavel ou mudança de fora não afeta função.

    ```
    function func1(){
        console.log("minha função");
    }
    
    ```

    - Podemos chama-la como variavel também:

    ```
    const func1 = function(){
        console.log("minha função 2");
    }
    
    ```

    - Criando funções por arrow functions(sempre criada dentro de váriaveis):

    ```
    const arrowTeste = () => {
        console.log("Essa é minha arrow");
    }
    
    ```

    - Arrowfunctions de uma linha só ( simples )
    Ao fazer a função que resolve uma raiz quadrade ele recebe um parametro x e já entende que deve retornar x*x sem precisar escrevermos

    ```
    const raizQuadrada = (x) => x*x
    
    ```


- Parâmetros: Qualquer valor usado dentro da função enviada de um contexto global.

    - Parâmetros Opcionais

        - Resolvendo com if 

        ```
        const multiplicacao = function(x,y){
            if(!y){
                return x*2
            }
            else{
                return x*y
            }
        }
        
        ```
        - Resolvendo com default
        
        ```
        const multiplicacao = function(x,y=2){
            return x*y
        }
        ```

        - Rest Operator: forma de enviar vários parametros sem defini-lo. Assim como o python tem o kwargs, porém o ...args vem em formato de lista.
        ```
        const somaInfinita = (...args) => {
            let total=0
            for(let i = 0; i < args.lenght; i++){
                console.log(i)
            }
        }
        ```



### Json encurtados, spreat e Desestruturação

Determinando as variáveis:

```
var nome = "maria";
var idade = 17
var empresa = {
    nome_empresa: "jusbrasil",
    cidade: "Salvador"
}

```
#### Json encurtado
Permite criar objeto json sem definir nome dos campos


Criando o json encurtado:

```
var user = {
    nome,
    idade, 
    empresa
}

```

#### Spread

Usando o exemplo de cima , caso eu quisesse chamar adicionar os campos de empresa individualmente em use o Spread me ajudaria, exemplo:
 
```
var user = {
    nome,
    idade, 
    ...empresa \\pega cada campo de empresa individualmente
}

```

#### Desestruturação

È o processo que permite recuperar campos dentro de um json e criar variáveis.

Ainda usando o user:

```
var user = {
    nome,
    idade, 
    ...empresa
}

```

Desestruturando esse json:


```
var{ nome, idade, cidade, nome_empresa} = user;

```
