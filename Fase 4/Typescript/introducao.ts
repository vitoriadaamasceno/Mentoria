const firstName = "João";
const lastName = "Silva";
const age = 30;

function greet(name:string){
    console.log(`Olá, ${name}!`);
}
greet(firstName);
greet(lastName);

console.log("-------------Tipos de dados------------------")
//Number
let x:number = 10
console.log(typeof x)
console.log(typeof 11.3)
//string

const primeiroNome:string = "mavi"
console.log(primeiroNome.toUpperCase())

let fullName:string
fullName = primeiroNome +  " damasceno"
console.log(fullName)


//Boleano
let a: boolean = false

console.log(a)
console.log(typeof a)

//Array

const lista: any[] = [1, 2, 3, "mavi", true];
console.log(lista)

const lista2: number[] = [1, 2, 3, 4, 5];
console.log(lista2)

//any
// Deve ser evitado, mas é usado quando não se sabe o tipo de dado
let valor: any = "mavi";
valor = 10;
console.log(valor);

function soma(a:number, b:number): number {
    return a+b
  }
console.log(soma(10, 20));
//Função com retorno void
function exibirMensagem(mensagem: string): void {
    console.log(mensagem);
}
exibirMensagem("Olá, Mavi!");

//Union

function exibirValor(valor: string | number): void {
    if (typeof valor === "string") {
        console.log(`O valor é uma string: ${valor}`);
    } else {
        console.log(`O valor é um número: ${valor}`);
    }
}
exibirValor("Olá");
exibirValor(42);
//Type
type Id = string | number;
function exibirId(id: Id): void {
    console.log(`O ID é: ${id}`);
}
exibirId("123");
exibirId(456);

//Interface
interface Pessoa {
    nome: string;
    idade: number;
    saudacao(): void;
}
function apresentarPessoa(pessoa: Pessoa): void {
    console.log(`Nome: ${pessoa.nome}, Idade: ${pessoa.idade}`);
    pessoa.saudacao();
}
apresentarPessoa({
    nome: "Mavi",
    idade: 25,
    saudacao: function() {
        console.log("Olá, eu sou a Mavi!");
    }
});

//Non-null assertion operator
let nomeCompleto: string | null = null;
nomeCompleto = "Mavi Damasceno";
console.log(nomeCompleto!.toUpperCase()); // O operador ! indica que nomeCompleto não é nulo
