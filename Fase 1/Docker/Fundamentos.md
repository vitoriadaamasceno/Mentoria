## Docker Fundamentos

Docker é a plataforma ideal para executar aplicações em **containers**, sendo containers uma técnica de virtualização(é uma tecnologia que permite criar vários ambientes simulados ou recursos dedicados ) eficiente a principal inovação do Docker é tornar essa tecnologia acessível a todos os desenvolvedores e administradores de sistema, de forma fácil, sem a necessidade de anos de prática para atingir a proficiência e sem a obrigação de serem desenvolvidas várias ferramentas personalizadas.

* Containers são unidades de software que empacota código e todas as dependências fazendo ela ser executada facilmente em qualquer configuração.

### Vantagens 

- Facilita o CI/CD
- Facilita a configuração de variáveis de ambiente
- Consistência entre o ambiente de desenvolvimento e de produção


**Os quatro principais conceitos para entender sobre o docker:**

1. Container :

O agrupamento de uma aplicação junto com suas dependências, são bem similares às máquinas virtuais, porém mais leves e mais integrados ao sistema operacional da máquina host, uma vez que, como já dissemos, compartilha o seu kernel, o que proporciona melhor desempenho por conta do gerenciamento único dos recursos.
 - Namespace: centraliza os processos 
 - cgroups: estabelece limites de uso de memória


2. Imagens:

Uma imagem do Docker, ou imagem de contêiner, é um arquivo executável independente usado para criar um contêiner. Essa imagem de contêiner contém todas as bibliotecas, dependências e arquivos de que o contêiner precisa para ser executado. Podemos usar imagens pronta direto ou usar elas como base para criar nossas proprias imagens.


3. Volumes 

São que diretórios externos ao container, que são montados diretamente nele. A principal função do volume é persistir os dados.

4. Dockerfile

O dockerfile nada mais é do que um arquivo onde você determina todos os detalhes do seu container, como, por exemplo, a imagem que você vai utilizar, aplicativos que necessitam ser instalados, comandos a serem executados, os volumes que serão montados, etc., etc., etc.!

[Docker HUb](https://hub.docker.com/)

[Documentação Docker ](https://docs.docker.com/reference/cli/docker/container/run/)

---

