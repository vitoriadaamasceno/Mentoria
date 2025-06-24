console.log(12*"abc")

console.log(10==10)
console.log(10===10)
console.log(10=="10")
console.log(10==="10")
console.log("-----------------------Diferentes-----------------")
console.log(10!=10)
console.log(10!==10)
console.log(10!="10")
console.log(10!=="10")

console.log("******************Mudança de tipo******************")
console.log(5*null)
console.log(5*undefined)
console.log(5*true)
console.log(5*false)
console.log("******************")
console.log("5" * 1)
console.log("5" - 2)
console.log("5" + 2)

console.log("******************USers******************")
var nome = "maria";
var idade = 17
var empresa = {
    nome_empresa: "jusbrasil",
    cidade: "Salvador"
}

var user = {
    nome,
    idade, 
    ...empresa 
}
console.log(user)

var{ nome, idade, cidade, nome_empresa} = user;
console.log(nome)
console.log(idade)
console.log(cidade)
console.log(nome_empresa)

console.log("*************Listas e Objetos***************")
var lista = [1,2,3,4,5];
console.log(typeof lista)
console.log(typeof user)
console.log(lista instanceof Array)
console.log(user instanceof Object)
console.log(lista instanceof Object)
console.log(user instanceof Array)

console.log("*************objeto***************")
const pessoa = {
    nome: "João",
    idade: 30,
    profissao: "Engenheiro"
}

var extra = {
    cidade: "São Paulo",
    estado: "SP"
}
console.log(pessoa.nome)
pessoa.idade = 31;
console.log(pessoa.idade)

var pessoaCompleta = Object.assign(pessoa, extra);
console.log(pessoaCompleta)

console.log(Object.keys(pessoaCompleta))

console.log(Object.values(pessoaCompleta))
console.log(Object.entries(pessoaCompleta))


console.log("*************foreach***************")
 
const posts = [
    { id: 1, titulo: "Post 1", conteudo: "Conteúdo do Post 1" },
    { id: 2, titulo: "Post 2", conteudo: "Conteúdo do Post 2" },
    { id: 3, titulo: "Post 3", conteudo: "Conteúdo do Post 3" }
];

posts.forEach((post) => {
    console.log(`Exibindo ${post.id} de titulo ${post.titulo}`)
})

var numeros = [1,2,3,4,5]
var listinha = []

numeros.forEach((num)=>{
    listinha.push(num)
})

console.log(listinha.includes(2))

console.log("------------Json--------------------")
var myJson = '{"name": "João", "idade": 30, "cidade": "São Paulo"}';
console.log(typeof myJson);
var parsedJson = JSON.parse(myJson);
console.log(parsedJson);
console.log(typeof parsedJson);