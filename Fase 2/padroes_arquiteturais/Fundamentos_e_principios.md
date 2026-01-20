# Arquitetura de software 

## Introdução a arquitetura de software 

**Tipos de arquitetura**

- software: Arquitetura de software faz parte da engenharia de software; Está diretamente ligada ao processo de desenvolvimento de software; Afeta e esta ligada a organização da empresa: como o time está formado, estrutura de componentes. Está ligado ao "como" como criar, manter e garantir que o desenvolvimento de sotware esteja alinhado com o negócio.

- solução: Fica entre o negócio e o sotware; Entende os requisitos e transforma em negócio; Deseja e planeja essa solução ( diagramas, UML, C4, BPMN); Analisa o mercado e os impactos comerciais.

- tecnológica: especialidade em tecnologias especificas, gera valor em cima de uma tecnologia especifica, planeja e define tecnologias.
Exemplo: Profissional especialista em Elastic.

- corporativa: É o processo pelo qual as organizações padronizam e organizam a infraestrutura de TI para se alinhar aos objetivos de negócios. È a prática de analisar, projetar, planejar e implementar a análise corporativa para executar com sucesso as estratégias de negócios incluindo custos, novas tecnologias, pluralidade de tecnologia com sabedoria e padronização.


### Diferença entre arquiteto de software e de soluções


Um arquiteto de soluções fornece o "o quê" e o "porquê" de um projeto (com foco geral nos negócios).

Por exemplo, escolher uma plataforma de nuvem, integrar diferentes sistemas e garantir que a solução atenda aos requisitos de negócios para escalabilidade, desempenho e segurança.

Um arquiteto de software fornece o "como" da implementação técnica.

Por exemplo, projetar o esquema do banco de dados, escolher frameworks e bibliotecas apropriados e definir os protocolos de comunicação entre diferentes componentes de software.

Algumas atribuições do arquiteto de software:

- Entender os requisitos e transformar em padrões arquiteturais.

- orquestrar o desenvolvimento ,desenvolvedores e cliente( seja diretamento ou através uma pessoa que entenda as necessidades e requisitos).

- Entender de forma profunda os modelos arquiteturais.

- Tomada de decisão e boas práticas de desenvolvimento.

- Ativo em code review.


### Arquitetura não é design 

Arquitetura: Escopo global ou alto nivel 

Design: Escopo global

Como assim? Arquitetura é uma visão macro, design é para decisões mais locais que nem sempre tem relação com o negócio.

### Pilares da arquitetura de software

- Estruturação que é como meu software consegue evoluir rápido, componentização para atender os objetivos do negócio.

- Componentização: dividir meu sotware em partes menores.

- Relacionamento entre sistemas: garantir a comunicação entre esses componentes e serem bem definidos.

- Governança: padronização, regras, comunicação, escolha de linguagens.


### Requisitos Arquitetural - tudo que preciso definir antes de iniciar a implantação

- Performance: preciso entender os limites do meu software, qual o máximo que ele vai consumir de memória, quantas replicas cada pod vai ter, rate limit.

- Armazenamento de dados: Onde vai ser armazenado? Qual tecnologia usaremos?

- Escalabilidade: Como ele vai escalar? Vai ser uma escala de aumento de dados, requisições ou uma escala de funcionalidades?

- Segurança: Certificações, criptografia, entender o quão delicado é os dados e qual tipo de segurança vai ser implementada.


- Legal: cumprir a legislação, seguir as definições LGPS.

- Auditoria

- Marketing: como vou fazer esse sotware chegar ao usuário

Entendemos que esses requisitos muitas vezes são implicitos porém é importante ter eles de forma clara.


### Caracteristicas arquiteturais



As Características Arquiteturais podem ser definidas como atributos fundamentais de um sistema, que devem, por si só, descrever toda a sua estrutura, comportamento e propriedades não funcionais.  Como modularidade(indepêndencia dos sistemas), escalabilidade, manutenibilidade, segurança, flexibilidade, disponibilidade(nivel de SLA), manutenibilidade.

#### Operacional

Disponibilidade: quanto tempo seu sistema ficará disponivel ? Quando ele não ficará disponível.


Recuperação de desastres: Em quanto tempo você consegue colocar seu sistema no ar de volta? Quem ficará responsável por monitorar a saúde do seu software?

Performance: Avaliar as possiveis demandas para usar as tecnologias que suportem. 

Backup: Como está sendo feito a recuperação de dados? você testou o backup.

Confiabilidade e Segurança


#### Arquitetural

- Configurável -> onde vão está minha variáveis de ambiente? Tenho facilidade para trocar alguma configuração.

- Expandível e de fácil instalação local: padronizar, permitir facilidade ṕara adição de serviços terceiros, uso de container.

- Reuso de componentes: evitar repetições


### Performance

È o desempenho que um software possui para completar determinada tarefa.

Como medimos performance?

- "Response time" : Quanto tempo demorar uma solicitação de uma requisição? Quando tempo demora para retornar dados?

- Throughput: Mostra o quanto de requisição simultânea o software.

Ter um sistema performatico não quer dizer que é escalavél.


#### Como medir performance?

- Diminuir a latência
    - Tempo de requisição em milisegundos
    - O tempo de processamento envolve processamento da aplicação, rede e chamadas externas.
 
-  Aumentando throughput
    - Quantidade de requisições simultâneas 


##### Erros que causam baixa performance

- Processamento ineficiente (falta de uso de queries, algoritmo, falta de caching para casos que precisam)

- Recurso computacional limitado

- Trabalhar de forma bloqueante(não conseguir lidar com diversas threads, requisições)


