# Hands-on: Docker Compose


### Entendendo o que é Docker Compose
È uma forma de escrever em apenas um arquivo todos os detalhes de sua aplicação, separando eles por serviços. Por exemplo, no Docker Compose nós definimos quais os services que desejamos criar e quais as características de cada service (quantidade de containers debaixo daquele service, volumes, network, secrets, etc.).


version: \"3\" -- Versão do compose que estamos utilizando.

services: -- Início da definição de meu serviço.

web: -- Nome do serviço.

image: nginx -- Imagem que vamos utilizar.

deploy: -- Início da estratégia de deploy.

replicas: 5 -- Quantidade de réplicas.

resources: -- Início da estratégia de utilização de recursos.

limits: -- Limites.

cpus: \"0.1\" -- Limite de CPU.

memory: 50M -- Limite de memória.

restart_policy: -- Políticas de restart.

condition: on-failure -- Somente irá "restartar" o container em caso de falha.

ports: -- Quais portas desejamos expor.

- \"8080:80\" -- Portas expostas e "bindadas".

networks: -- Definição das redes que irei utilizar nesse serviço.

- webserver -- Nome da rede desse serviço.

networks: -- Declarando as redes que usaremos nesse docker-compose.

webserver: -- Nome da rede a ser criada, caso não exista.

https://livro.descomplicandodocker.com.br/chapters/chapter_15.html
