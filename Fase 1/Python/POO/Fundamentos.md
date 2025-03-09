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
    - **o python não tem nada reservado para proteger essa varivel mas por convenção usamos o _**
    - Publico = pode ser acessado fora da classe
    - Privado =  só pode ser acessado pela classe
    - Propedies
        cria atributos gerenciados, usa atributos gerenciados quando precisar mudar algo internamente 


3. Polimorfismo: O mesmo nome de função porém com assinaturas diferentes , ou seja um dado tenho muitas formas.Definimos Polimorfismo como um princípio a partir do qual as classes derivadas de uma única classe base são capazes de invocar os métodos que, embora apresentem a mesma assinatura, comportam-se de maneira diferente para cada uma das classes derivadas.

    - a funçao len é um exemplo de polimorfismo nativo, caso a gente passe uma lista ele conta os elementos da lista, caso for uma string conta os caracteres


4. Interfaces e classes abstratas

    - atributos de classe são compartilhados entre todas as instâncias da classe
    - atributos de instância são específicos de cada instância da classe
    - metodos de classes: esta ligado a classe e não ao objeto, ele chama cls e não self( convenção), tem acesso ao estado da classe
    - metodos estaticos: È vinculado a classe e não ao objeto , porém não acessa o estado da classe, faz sentido dentro da classe
    - Diferença entre os metodos:
        - O metodo de classe recebe o parametro que aponta pra classe  e o estático não.

        - O de classe muda o estado da classe o estático não altera e nem pode acessar


    4.1 Intefaces; Definem o que uma classe deve fazer e não como ela deve fazer , todo mundo pode usar mas o como é da sua forma

        - Em python a interface é definir uma contrato onde são declarados os metodos ( o que deve ser feito), e suas assinatiras usando classes abstratas para criar ccontratos

        - Classes abstratas não podem ser instanciadas 

    
    4.2 Classes abstratas: Por padrão python não oferece classes abstratas , mas existe um modulo (ABC) que fornece a base para definir essas classes.É um tipo de classe especial que não pode ser instanciada, apenas herdada. Sendo assim, uma classe abstrata não pode ter um objeto criado a partir de sua instanciação. Essas classes são muito importantes quando não queremos criar um objeto a partir de uma classe “geral”, apenas de suas “subclasses.


    Vimos então que as classes abstratas e interfaces possuem algumas características semelhantes (não podem ser instanciadas, possuem métodos abstratos que obrigam as outras classes a implementá-los), porém elas não servem para o mesmo propósito.

    Quando utilizamos as interfaces, estamos definindo um conjunto de assinatura de métodos que outras classes devem implementar. Com isso, apenas definimos o comportamento base de um conjunto de classes que, por ventura, implementem esta interface.

    Já as classes abstratas servem para prover uma base para que as classes que “herdem” desta não precisem se preocupar com o comportamento padrão, apenas com suas características e comportamentos pessoais.
    Sendo assim, sempre que precisarmos definir um conjunto de métodos que devem ser implementados por um grupo de classes, utilizamos as interfaces. Se precisarmos determinar uma classe base para outras classes, que herdarão seus atributos e métodos e esta classe não deva ser instanciada, utilizamos as classes abstratas.


    