# Conceitos REST

### O que é 

Rest è Representational State Transfer que significa Transferência de Estado Representacional. Sendo principios e definições necessário para criação de um projeto web padronizados e bem definidos.
É, na verdade, uma abstração da arquitetura da Web(WWW). Por ser muito requisitada nas equipes de desenvolvimento, é importante se aprofundar nos estudos desse recurso.

Quando se abre o navegador, o Rest estabelece uma conexão TCP/IP com o servidor de destino. Ele envia uma requisição GET HTTP a partir do endereço informado > o servidor enviar a resposta HTTP e resposta é formata para HTML

https://mailchimp.com/pt-br/resources/rest-api/


### Qual a sua importância

1- Ao utilizar Rest é possível perceber uma melhora nos fluxos. Isso porque as aplicações web que utilizam Rest são mais flexíveis, leves e permitem melhores resultados quando se utiliza metodologia ágil.

2- facilitam a comunicação entre diferentes sistemas de software, permitindo que eles troquem dados de forma padronizada e atuando juntos. Algumas de suas utilidades são a conexão entre sistemas criado por diferentes empresas, permitindo a comunicação e o compartilhamento de informações.


### Diferença entre Rest e Restful

Rest: é um conjunto de princípios de arquitetura.
Restful: é uma condição única de aplicar os conceitos de Rest, ou seja, capacidade de fazer rest.
Enquanto o primeiro está voltado à criação de serviços disponibilizados na web, o segundo é aquele que realiza a implementação desse padrão.


### REST vs. SOAP vs. GraphQL

Imagine que você está construindo uma casa: REST API , GraphQL e SOAP são como conjuntos diferentes de plantas de construção, cada um com seu próprio estilo e abordagem.
São regras de como uma aplicação web irá se comunicar, enviar e receber dados.

- Rest

Usa solicitação HTTP através de verbos como GET, PUT, POST e DELETE.  é construída no protocolo REST. No desenvolvimento de serviços web, REST é um estilo arquitetônico e técnica de comunicação popular.

- GraphQL

È como se fosse uma linguagem especial para pedir informações a um site ou aplicativo. Quando você envia uma pergunta usando GraphQL, o servidor descobre o que você está procurando, encontra as informações certas e as envia de volta. Ao contrário do REST, onde você pode precisar pedir coisas de diferentes pontos, o GraphQL permite que você geralmente obtenha tudo o que precisa de uma só vez.
    
    https://docs.github.com/pt/graphql/guides/forming-calls-with-graphql


- SOAP

É basicamente um protocolo de comunicação web que foi criado para a Microsoft em 1998. Hoje em dia, os principais usos para ele são transmissão de dados HTTP/HTTPS e exposição de serviços web.  Ao contrário do padrão REST, o SOAP suporta apenas o formato de dados XML 

https://www.geeksforgeeks.org/rest-api-vs-graphql-vs-soap/