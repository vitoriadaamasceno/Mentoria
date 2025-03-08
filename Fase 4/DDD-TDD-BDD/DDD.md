# DDD - Domain-Driven Design 

### Conceito

 È uma **abordagem** focado no design de software usando uma serie de protocolos, técnicas e conceitos para garantir a eficência no desenvolvimento, ou seja, ele alinha o software com a aréa de interesse dele, onde reside o problema.
 Para usar DDD no seu software é necessário dominar as regras de négocio do seu sistema , pois o objetivo é deixar o mais próximo possivel do problema a ser resolvido.

 Desenvolver um modelo de domínio envolve identificar as entidades, objetos de valor, agregados e serviços de domínio que compõem o domínio do problema. 


### Objetivo

    O Domain-Driven Design traz uma série de técnicas importantes para realizar um design impecável de software, conseguindo unir funcionalidade, experiência do usuário e visual atrativo para o usuário final. Sua abordagem deve ser eficaz a ponto de ter um bom design de software mas não deixar de atender as demandas e funções a serem cumpridas.

    Seu principal objetivo é manter o foco no Domínio de Software de uma maneira automatizada.
    O DDD **não é sobre dividir a aplicação em camadas responsáveis**, o DDD é sobre modelar corretamente o domínio do seu negócio. 
    Se sua aplicação possui uma única camada de domínio e esta camada concentra todas as entidades do seu negócio você pode estar cometendo um grande erro de modelagem de domínio. Para aplicações que possuem domínios muito complexos o ideal é aplicar o conceito de Bounded Context(É o foco da seção de design estratégico do DDD).


### O modelo DDD apresenta 5 itens principais:

1. Entidades: identificar as entidades que são objetos no dominio que tem uma identidade única(id) possuindo atributos e comportamentos ( metodos). Entidades podem ter relacionamentos com outras entidades no domínio. Por exemplo, na plataforma de e-commerce, um produto seria uma entidade. Cada produto teria um identificador único e atributos como nome, descrição, preço e disponibilidade. 

2. Objetos de valor: Um objeto que agrega valor às entidades, não possui identidade e é imutável.Por exemplo, na plataforma de e-commerce, uma avaliação de produto seria um objeto de valor. Cada avaliação teria atributos como a classificação, o texto da avaliação e a data em que foi publicada.Eles podem ser usados ​​como atributos de entidades ou como objetos autônomos no domínio. 

3. Factories: Classe responsável por construir adequadamente um objeto / entidade.

4. Serviços: Serviço do domínio que atende partes do negócio que não se encaixam em entidades específicas, trabalha com diversas entidades, realiza persistência através de repositórios e etc.Por exemplo, na plataforma de e-commerce, um pedido seria um agregado. Um pedido consistiria em um ou mais itens de linha, cada um dos quais seria uma entidade. 

5. Repositorios: Uma classe que realiza a persistência das entidades se comunicando diretamente com o meio de acesso aos dados, é utilizado apenas um repositório por agregação.

6. Agregados: são grupos de entidades relacionadas e objetos de valor que são tratados como uma única unidade. Por exemplo, na plataforma de e-commerce, um pedido seria um agregado. Um pedido consistiria em um ou mais itens de linha, cada um dos quais seria uma entidade. 


### Além disso aborda outros pontos:

1. ubiquitous language (linguagem onipresente): é a adequação para a linguagem do negócio. Por exemplo, se a solução será desenvolvida para o setor financeiro, termos como “amortização de dívidas” e “antecipação de recebíveis” deverão se repetir, tanto no modelo quanto no código, fazendo com que todos falem a língua do negócio;

2. separação das camadas: as camadas da solução precisam ser independentes, sem se misturarem.³

3. bounded Contexts “contextos delimitados”: Isto significa que você deve delimitar as intenções de suas entidades com base no contexto que ela pertence.
    exemplo:
        Quando se pergunta sobre um funcionário no departamento de TI este está ligado a um usuário e suas responsabilidades dentro do sistema, quando se pergunta sobre um funcionário dentro do RH este está ligado a um colaborador da empresa. É a mesma pessoa, porém dentro da aplicação possui intenções diferentes e é baseada nas intenções que o seu domínio deve ser delimitado em contextos. Não tem necessidade nenhuma a entidade Funcionário do o bounded context de TI ter acesso a salário, reajustes e etc.

4. Domain Expert: É a pessoa que entende do negócio da empresa e vai apoiar os times de desenvolvimento na modelagem do domínio, definição das regras de negócio e etc.

5. Big Ball of Muda ( grande bola de lama):A grande bola de lama. Você pode ter uma em suas mãos neste momento;Este conceito aborda vários aspectos negativos de sua aplicação, desde código macarrônico que fere os princípios do SOLID e Clean Code até uma entidade com muitas responsabilidades em um único contexto.



Obs ¹: cumprir o propósito que a aplicação deve atender

Obs ²: O que significa visão global do domínio?
Ter uma visão global significa enxergar toda a extensão de seu domínio e eu não estou me referindo as camadas, estou me referindo ao negócio.


[mais sobre](https://www.eduardopires.net.br/2016/03/ddd-bounded-context/)