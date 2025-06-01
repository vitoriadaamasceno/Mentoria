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
