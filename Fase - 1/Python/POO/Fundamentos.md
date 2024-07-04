# POO


Programação orientada a objetos é um paradigma ou seja um exemplo que serve como modelo; padrão de estrutura de código seu principal objetivo é abstrair problemas em objetos do mundo real , tornando seu código mais légivel e expansível. Sendo seus dois conceitos chaves classes e objetos.

### Classes e Objetos - Conceito

Uma classe definir as caracteristas e comportamentos de um objetos porém não usamos ela diretamente, já o objeto é possivel user e possui as mesmas caractectistas e comportamnentos descrita na classe

### Construtores e destrutores

    Metodo construtor : é chamada sempre que instanciamos um objeto de uma classe, e nele é inicializado o estado desse objeto esse metodo é criado utilizando o `__init__`  


    Metodo destrutor é executado quando o objeto é destruido , no Python ele não é tão necessario pois ele lida com esse gerenciamento de memória automaticamente , usamos o metodo destrutor através do `__del__` 


## Tipos


1. Herança: capacidade de definir uma classe filha para derivar/herdar da classe "pai"

    - Permite reutilização de código( se for bem utilizada)
    - Representa bem o mundo real 
    - Evitar usar uma muitas camadas de reutilização
    - Herança simples e multiplas


2. Encapsulamento: È a ideia de agrupar dados e metodos que manipulam esses dados , uma especie de proteção a esses dados para que nem todo mundo possa manipula-lo

    - Exemplo real: você tem uma aplicação para cadastro de produto, em que seu app tem um bug quando você cadastra um produto de 20,00 e toda vez que eu cadastro ele salva como 10,00. Dentro do meu código a varias partes que mexe com a variavel produto, eu teria que verificar todos pra vê se algum está alterando isso , com o encapsulamento eu posso ter um metodo protegido para cadastro , então ngm pode acessar diretamente o valor só através de metodos publicos 
    - o python não tem nada reservado para proteger essa varivel mas por convenção usamos o _
    - Publico = pode ser acessado fora da classe
    - Privado =  só pode ser acessado pela classe
    - Propedies
        cria atributos gerenciados, usa atributos gerenciados quando precisar mudar algo internamente 


3. Polimorfismo: O mesmo nome de função porém com assinaturas diferentes , ou seja um dado tenho muitas formas

    - a funçao len é um exemplo de polimorfismo nativo, caso a gente passe uma lista ele conta os elementos da lista, caso for uma string conta os caracteres


4. Interfaces e classes abstratas
