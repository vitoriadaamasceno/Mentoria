### JWT 

Vamos falar um pouco sobre JWT e com proteger sua aplicação. 

##### O que é JWT e onde ele se conecta com o assunto de API REST?

JWT (JSON Web Token) é um padrão aberto (RFC 7519) para transmissão segura de informações como objeto JSON entre partes. Ele é amplamente usado para autenticação e autorização em aplicações web. O JWT é composto por três partes codificadas em Base64:

Header: Contém o tipo do token (JWT) e o algoritmo de assinatura (ex: HS256).

Payload: Contém as claims, ou seja, as informações que estão sendo transmitidas (como ID do usuário, permissões, etc.).

Signature: É uma assinatura digital criada com base no header e no payload, usando uma chave secreta (ou par de chaves pública/privada, no caso de RS256).

Dentro da API REST o JWT é usado para autentificação e autorização do usuário. Onde o usuário enviar suas credenciais  a api valida e gera um JWT, ele retorna ao cliente onde vai ser armazenado autorizando o acesso dele nas rotas/páginas.

##### Tipo

Access Token -> enviado a da requisição para autentificação do usuário.

Refresh Token -> Permite renovar o acesso sem precisar loggar novamente.

#### Afinal, onde armazenar os tokens?

Lembrando que não existe certo ou errado, tudo depende da complexidade/contexto e nivél de segurança necessário para sua aplicação. Sabendo que cada um tem suas vunerabilidades.

- Session Storage

Armazena chave e valor no session storage do seu browser. Os dados salvos são temporarios ao fechar o browser essa autentificação não é mais valida.

Possíveis ataques:

XSS - tentar injetar script no seu código
LIB - com vunerabilidade
Query params - falta de filtragem que pode acabar trazendo alguma informação

Sendo necessário usar Content Policy

- Local Storage

- Cookies



