# DDD - Domain-Driven Design 

### Conceito

 È uma abordagem focado no design de software usando uma serie de protocolos, técnicas e conceitos para garantinha eficência no desenvolvimento.

### Objetivo

    O Domain-Driven Design traz uma série de técnicas importantes para realizar um design impecável de software, conseguindo unir funcionalidade, User Experience e visual atrativo para o usuário final. Sua abordagem deve ser eficaz a ponte de ter um bom design de software mas não deixar de atender as demandas e funções a serem cumpridas.

    Seu principal objetivo é manter o foco no Domínio de Software¹ de uma maneira automatizada.
    O DDD não é sobre dividir a aplicação em camadas responsáveis, o DDD é sobre modelar corretamente o domínio do seu negócio. Se sua aplicação possui uma única camada de domínio e esta camada concentra todas as entidades do seu negócio você pode estar cometendo um grande erro de modelagem de domínio. Para aplicações que possuem domínios muito complexos o ideal é aplicar o conceito de Bounded Context.


### O modelo DDD apresenta 5 itens principais:

1. Entidades

2. Objetos de valor :Um objeto que agrega valor às entidades, não possui identidade e é imutável.

3. Factories:Classe responsável por construir adequadamente um objeto / entidade.

4. Serviços: Serviço do domínio que atende partes do negócio que não se encaixam em entidades específicas, trabalha com diversas entidades, realiza persistência através de repositórios e etc.

5. Repositorios: Uma classe que realiza a persistência das entidades se comunicando diretamente com o meio de acesso aos dados, é utilizado apenas um repositório por agregação.


Além dsso aborda outros pontos:

1. ubiquitous language (linguagem onipresente): é a adequação para a linguagem do negócio. Por exemplo, se a solução será desenvolvida para o setor financeiro, termos como “amortização de dívidas” e “antecipação de recebíveis” deverão se repetir, tanto no modelo quanto no código, fazendo com que todos falem a língua do negócio;

2. separação das camadas: as camadas da solução precisam ser independentes, sem se misturarem.³

3. bounded Contexts “contextos delimitados”: Isto significa que você deve delimitar as intenções de suas entidades com base no contexto que ela pertence.
    exemplo:
        Quando se pergunta sobre um funcionário no departamento de TI este está ligado a um usuário e suas responsabilidades dentro do sistema, quando se pergunta sobre um funcionário dentro do RH este está ligado a um colaborador da empresa. É a mesma pessoa, porém dentro da aplicação possui intenções diferentes e é baseada nas intenções que o seu domínio deve ser delimitado em contextos. Não tem necessidade nenhuma a entidade Funcionário do o bounded context de TI ter acesso a salário, reajustes e etc.

4. Domain Expert: É a pessoa que entende do negócio da empresa e vai apoiar os times de desenvolvimento na modelagem do domínio, definição das regras de negócio e etc.

5. Big Ball of Muda ( grande bola de lama):A grande bola de lama. Você pode ter uma em suas mãos neste momento;Este conceito aborda vários aspectos negativos de sua aplicação, desde código macarrônico que fere os princípios do SOLID e Clean Code até uma entidade com muitas responsabilidades em um único contexto.

6. 


Obs ¹: cumprir o propósito que a aplicação deve atender

Obs ²: O que significa visão global do domínio?
Ter uma visão global significa enxergar toda a extensão de seu domínio e eu não estou me referindo as camadas, estou me referindo ao negócio.


[mais sobre](https://www.eduardopires.net.br/2016/03/ddd-bounded-context/)