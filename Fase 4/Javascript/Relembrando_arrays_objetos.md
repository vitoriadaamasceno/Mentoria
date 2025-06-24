## Arrays e Objetos


### Arrays

Arrays são listas inseridos entre cochetes e separados por virgulas.
Em JS um array é do tipo Object.

- Propriedades

```
lista = [1,2,3]

//Quantos items tem em uma lista?
lista.lenght
ou 
lista['length']

//Acessar valor

lista[0]

```

- Metodos(objetos são compostos por metodos e propriedades de acordo com OOP)
    Alguns metodos 
    - push e pop -> remove valores do final e adiciona
    - shift e unshift -> remove e adiciona valores do final.
    - indexOf e lastIndexOf -> mostra o indice de um elemento , e lastindex indice da ultima ocorrência
    


1. Concatenar arrays

```
const numberOther = [1,2,3]

const all = lista.concat(numberOther)

```

### Objetos 

- Estilo um dicionario de python. Um dado que possui chave e valor.
- **Um objeto ou array criado como const pode ser ter seus elementos o propriedade modificados.**
- O object literal é uma instância de um objeto, chamado Object.

```
const person = {
    name: "mavi"
    idade: 25
}

```

Alterando idade;

```
person.idade = 26

```
 
- Metodo assign

```
const obj = {
    a: "teste",
    b: true,
};

const obj2 = {
    c:[]
}

console.log(obj instanceof Object); //olha se é uma instância

teste = Object.assing(obj, obj2)
```

### Diferença entre arrays e objetos pra o JS


Arrays são utilizado no modo lista onde não importa muito a descrição daquele valor. Já os objetos descrevem melhor os valores, e aceitam diferentes tipos de dados.
Pode existir também arrays de objetos. Dentro do js o tipo é o mesmo.


### forEach


Uma forma mais limpa de fazer for e while com arrow functions

```
var numeros = [1,2,3,4,5]
var listinha = []

numeros.forEach((num)=>{
    listinha.push(num)
})

```
