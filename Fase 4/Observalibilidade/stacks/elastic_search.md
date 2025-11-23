## Stacks


Vamos conhecer algumas stacks de observabilidade.

### Elastic Stack

Primeira vamos entender o que é algumas stacks relacionadas:

- Elasticsearch, basicamento é uma aplicação de search engine e analytics onde você consegue inserir dados lá e ele vai fazer busca e analisar esse dados de maneira rápida.De maneira bem resumida ele permite armazenar, buscar e analisar grandes volumes de dados (estruturados, não estruturados e vetoriais) em tempo real.

- Logstash é um processador de dados através de pipelines que consegue receber, transformar e enviar dados simultaneamente. Os dados são enviados para o Elasticsearch. le opera como um pipeline, onde o "Input" recolhe os dados, os filtros "Filter" os transformam e enriquecem e o "Output" envia-os para um local de destino. É uma parte central do Elastic Stack (composto também por Elasticsearch e Kibana), servindo para processar e unificar dados de logs, métricas e aplicações de forma dinâmica e em tempo real. 

- Kibana : permite o usuário visualizar os dados do elastic search em diversas perspectivas.

Os três juntos formam o elastic search , que tem diversos beneficios como por exemplo:

- Rapidez (extremamente rápido)

- Escalável

- API Rest ( prover api rest o que facilita seu uso)

- Análise e visualização geoespacial

- Aplicação, site, website , enterprise search

- Considerando que ele é muito bom para pesquisar, buscas rápidas porque não usa-lo para guardar loggings e analytics. Sendo muito mais simples para busca-los.


obs : aprofundar depois