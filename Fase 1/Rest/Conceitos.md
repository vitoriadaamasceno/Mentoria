# Conceitos REST

### O que é 

Rest è Representational State Transfer que significa Transferência de Estado Representacional. Sendo principios e definições necessário para criação de um projeto web padronizados e bem definidos.
É, na verdade, uma abstração da arquitetura da Web(WWW). Por ser muito requisitada nas equipes de desenvolvimento, é importante se aprofundar nos estudos desse recurso.

Quando se abre o navegador, o Rest estabelece uma conexão TCP/IP com o servidor de destino. Ele envia uma requisição GET HTTP a partir do endereço informado > o servidor enviar a resposta HTTP e resposta é formata para HTML

https://mailchimp.com/pt-br/resources/rest-api/


### Qual a sua importância

1 - Agilidade = Ao utilizar Rest é possível perceber uma melhora nos fluxos. Isso porque as aplicações web que utilizam Rest são mais flexíveis, leves e permitem melhores resultados quando se utiliza metodologia ágil.

2 - Multi dispositivos e multicanal = pode ser usado em vários dispositivos diferentes.

3 - Exposição do seu négocio = facilitam a comunicação entre diferentes sistemas de software, permitindo que eles troquem dados de forma padronizada e atuando juntos. Algumas de suas utilidades são a conexão entre sistemas criado por diferentes empresas, permitindo a comunicação e o compartilhamento de informações.

4 - Padronização facilitando toda a complexidade por trás daquilo.


### Diferença entre Rest e Restful

- Rest: é um conjunto de princípios de arquitetura.

- Restful: é uma condição única de aplicar os conceitos de Rest, ou seja, capacidade de fazer rest.
Enquanto o primeiro está voltado à criação de serviços disponibilizados na web, o segundo é aquele que realiza a implementação desse padrão.


### REST vs. SOAP vs. GraphQL

Imagine que você está construindo uma casa: REST API , GraphQL e SOAP são como conjuntos diferentes de plantas de construção, cada um com seu próprio estilo e abordagem.
São regras de como uma aplicação web irá se comunicar, enviar e receber dados.

- Rest

Usa solicitação HTTP através de verbos como GET, PUT, POST e DELETE.  é construída no protocolo HTTP. No desenvolvimento de serviços web, REST é um estilo arquitetônico e técnica de comunicação popular.

- GraphQL

È como se fosse uma linguagem especial para pedir informações a um site ou aplicativo. Quando você envia uma pergunta usando GraphQL, o servidor descobre o que você está procurando, encontra as informações certas e as envia de volta. Ao contrário do REST, onde você pode precisar pedir coisas de diferentes pontos, o GraphQL permite que você geralmente obtenha tudo o que precisa de uma só vez.
    
    https://docs.github.com/pt/graphql/guides/forming-calls-with-graphql


- SOAP

É basicamente um protocolo de comunicação web que foi criado para a Microsoft em 1998. Hoje em dia, os principais usos para ele são transmissão de dados HTTP/HTTPS e exposição de serviços web.  Ao contrário do padrão REST, o SOAP suporta apenas o formato de dados XML .

https://www.geeksforgeeks.org/rest-api-vs-graphql-vs-soap/


2. Métodos HTTP 

Os principais verbos/metodos HTTP incluem:

GET – Recupera dados do servidor, pode usar cache, não altera estado. -> 200
POST – Envia dados para criação de um recurso, normalmente não usa cache e retorna o id -> 201
PUT – Atualiza um recurso por completo caso esse valor não exista cria, ele altera o estado, geralmente não usa cache. -> 200
PATCH – Atualiza um recurso parcialmente, geralmente usado para apenas um campo ou seja uma instância -> 200
DELETE – Remove um recurso. -> 204 - No content e uma mensagem de sucesso
OPTIONS – lista todos os verbos possivéis para um recurso
HEAD – para retornar cabeçalhos.

Acesse outros:  https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Methods


3. Boas práticas e principios arquiteturais

Basicamente a API rest tem 4 pilares para está bem feita : documentação, nomeclatura, verbos ,status.


*Boas práticas:*

- Cuidado com as resposta de status sempre procure a que tem mais haver com resposta( sempre pense se a pessoa entenderia o que houve apenas com o status)
- Endpoints devem ser compostos unicamente por nomes, não use verbos;
- Utilize kebab-case para palavras compostas;
- Nomear os endpoints por recursos e respeitando os plurais;
- Organize os recursos por hierárquias;
- Versione seus contratos;
- Dominio da API deve ser diferente do site;
- Use letras minúsculas;
- Não termine seus endpoints com “/”;
- Use diferentes verbos HTTP para suas operações. Por exemplo, POST é usado para criar um Recurso.


*Principios Arquiteturais:* 

- Cliente/Servidor = O cliente tem relação com a interface e experiência do usuário, já o servidor tem relação com a performance , autorização , autentificação, segurança, cache.

- Interface Uniforme é uma especie de contrato sobre recursos, mensagens, metadados.

- Rest é statelessness ou seja não tem estado , não armazena sessão ou qualquer dado de requisição anterior. São requisições independentes.

- Uso de cache por ser statelessness é necessário usar cache para compensar a perda de performance e diminuir a quantidade de requisições e de trafego de rede. Esse cache é controlado via headers: cache-control, expires, last-modified.

- Sistema de camadas para acessar um dado.


4. Segurança na API Rest


4.1  Autenticação e Autorização (OAuth2, JWT, Basic Auth)


- Autenticação: é quando uma entidade prova uma identidade, ou seja, é a prova de que você é quem diz ser.

- Autorização: é quando uma entidade prova um direito de acesso, ou seja, prova que você tem o direito de fazer uma solicitação.

Autenticação refere-se à comprovação de identidade correta e autorização refere-se à permissão de uma determinada ação.


Tipos de Autenticação:

*Basic:*

- Pouca segurança 
- Este é o método mais direto e fácil. 
- o remetente coloca um username:password no cabeçalho da solicitação. O username e a password são codificados com Base64.
- Não requer cookies, id de sessão ou página de login nem nada complexo.


*Portador - Bearer:*

- Ao invés de autenticar a senha autenticamos o token do portador.
- O token do portador permite acesso a um determinado recurso ou URL e muito provavelmente é uma string criptografada, geralmente gerada pelo servidor em resposta a uma solicitação de login.

*OpenId Connect:*

- Permite que o sistema A acesso o sistema B em nome do cliente sem que o sistema A tenha acesso a senha e usuário. Como login pelo Google..

*Auth2.0:*

- Confiar em um Security Token Service para validar o token das credenciais do usuário.

*JWT*

- é um método seguro de autenticação e autorização, que fornece uma maneira de transmitir informações seguras entre duas partes. O JWT é baseado em um formato de token autônomo que pode ser facilmente verificado e decodificado. Ele é uma alternativa mais segura ao token de autenticação padrão.


-> Boas Práticas

1. Limite as tentivas de login
2. Criptografia de senhas e token

https://www.dio.me/articles/autenticacao-e-autorizacao-de-uma-api
https://blog.restcase.com/4-most-used-rest-api-authentication-methods/


5. HETEOAS(pouco adotado)

A intenção do REST é que a API seja semelhando ao acesso a WEB ou seja que um link leve ao outro. O HETEAOS deve funcionar como um provedor de links ou seja ao acessar um endpoint ele me leve a outros. A API retroalimenta ela mesma.


6. Modelagem

È o processo de entender a regra de negócio e transforma-la em recursos para seus endpoints, respeitando os padrões do REST. Quando não puder fazer o REST puro deixar o mais proóximo possivél. 
- A modelagem deve sempre olhar para os clientes (quem vai consumir) e não para os dados.
- Foque nas principais e evite repetições de endpoints que fazem a mesma coisa.
- Evite respostas json's muito complexas.
- Entender as entidades e seus relacionamentos.
- O DDD é um aliado para o REST já que ele fornece recursos e padroes que ajuda a documentar e modelar nos padrões REST.

Passo a passo:

    1. Listar os requisitos do negócio
    2. Indentificar quem são as entidades
    3. Indentificar os serviços -> funções que não entididades mas são necessárias
    4. Fazer Domain Model -> Desenhar entidades, serviços, relacionamentos e bounded contexts
    5. Converter em REST seu Domain Model



7. Versionamento
 
Pode ocorrer por quebra de contrato, mudança de regra de negocio, alteração de contrato,semântica inversa.
Sempre que houver uma mudança que atinge o usuário ou alteração de contrato é necessário criar duas versões.

3 estágios: 1 patch não altera só acrescenta, 3 minor não causa erro para o cliente, 2 quebra de contrato.

Estratégia de migração: a melhor maneira é tranformar minha v1 em um proxy para minha v2.

8. Formatos API-REST

*JSON x XML*

Json é um objeto de formato aberto que pode ser lido por pessoas ou máquins com facilidade e em qualquer linguagem. Já o XML é uma linguagem de marcação que fornece regra pra definir qualquer tipo de dado, usando tags para diferenciar atributos de dados reias.
Ambos podem ser transformados de acordo com a linguagem porém o JSON é muito mais simples e flexivel.

Se você quiser armazenar vários tipos de dados diferentes com muitas variáveis, o XML é a melhor opção. O XML verifica erros em dados complexos com mais eficiência do que o JSON, pois o XML se concentra em armazenar dados que sejam legível por máquinas. Ele também tem um conjunto mais maduro de ferramentas e bibliotecas e pode funcionar melhor com sistemas herdados.Por outro lado, o JSON foi projetado para o intercâmbio de dados e fornece um formato mais simples e conciso. Ele também melhora a performance e a velocidade da comunicação.


9. Negociação de conteúdo

As negociações de conteudo é o mecanismo usado para servir diferentes representações de um recurso

O Accept cabeçalho sempre indica que tipo de resposta do servidor um cliente pode aceitar. Content-Typeé sobre o conteúdo da solicitação ou resposta atual, dependendo do tipo de mensagem HTTP aplicada.

Portanto, se uma solicitação não tiver carga útil, você não precisará enviar um Content-Typecabeçalho de solicitação, e o mesmo vale para sua resposta: sem corpo — sem cabeçalho necessário.


10. Rest x gRPC

gRPC e REST são duas abordagens diferentes para o desenvolvimento de APIs.

**gRPC** é uma arquitetura e um sistema de API baseado em RPC que se trata de comunicações cliente-servidor funcionam como se as solicitações da API do cliente fossem uma operação local ou como se a solicitação fosse um código interno do servidor. Na RPC, um cliente envia uma solicitação para um processo no servidor que está sempre ouvindo chamadas remotas. Na solicitação, ele contém a função do servidor a ser chamada, junto com todos os parâmetros a serem transmitidos. Uma API RPC usa um protocolo como HTTP, TCP ou UDP como o mecanismo subjacente de troca de dados, o gRPC é semelhante porém ele usa  buffers de protocolo e HTTP 2 para a transmissão de dados.

Tanto a gRPC quanto a REST usam o seguinte: 
Comunicação assíncrona, para que o cliente e o servidor possam se comunicar sem interromper as operações
Design sem estado, para que o servidor não precise se lembrar do estado do cliente.