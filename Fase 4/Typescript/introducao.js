"use strict";
const firstName = "João";
const lastName = "Silva";
const age = 30;
function greet(name) {
    console.log(`Olá, ${name}!`);
}
greet(firstName);
greet(lastName);
console.log("-------------Tipos de dados------------------");
//Number
let x = 10;
console.log(typeof x);
console.log(typeof 11.3);
//string
const primeiroNome = "mavi";
console.log(primeiroNome.toUpperCase());
let fullName;
fullName = primeiroNome + " damasceno";
console.log(fullName);
//Boleano
let a = false;
console.log(a);
console.log(typeof a);
//Array
const lista = [1, 2, 3, "mavi", true];
console.log(lista);
const lista2 = [1, 2, 3, 4, 5];
console.log(lista2);
//any
// Deve ser evitado, mas é usado quando não se sabe o tipo de dado
let valor = "mavi";
valor = 10;
console.log(valor);
function soma(a, b) {
    return a + b;
}
console.log(soma(10, 20));
//Função com retorno void
function exibirMensagem(mensagem) {
    console.log(mensagem);
}
exibirMensagem("Olá, Mavi!");
//Union
function exibirValor(valor) {
    if (typeof valor === "string") {
        console.log(`O valor é uma string: ${valor}`);
    }
    else {
        console.log(`O valor é um número: ${valor}`);
    }
}
exibirValor("Olá");
exibirValor(42);
function exibirId(id) {
    console.log(`O ID é: ${id}`);
}
exibirId("123");
exibirId(456);
function apresentarPessoa(pessoa) {
    console.log(`Nome: ${pessoa.nome}, Idade: ${pessoa.idade}`);
    pessoa.saudacao();
}
apresentarPessoa({
    nome: "Mavi",
    idade: 25,
    saudacao: function () {
        console.log("Olá, eu sou a Mavi!");
    }
});
//Non-null assertion operator
let nomeCompleto = null;
nomeCompleto = "Mavi Damasceno";
console.log(nomeCompleto.toUpperCase()); // O operador ! indica que nomeCompleto não é nulo
