## Noções de Internet

- Como a Internet funciona? ✨

O que é ?

Entendendo que rede é um grupo de computadores conectados que são capazes de enviar dados uns para os outros como um grupo de amigos em um circulo social.
A palavra internet deriva do conceito interconexões de redes, ou seja, é uma vasta e espalhada coleção de redes que se conectam umas ás outras. Dessas forma podemos nos comunicar através do computadores porque estão dentro dessas redes que também estão conectadas.
Todos os dados enviados pela internet são traduzidos em pulsos de luz ou eletricidade, também chamados de "bits," e depois interpretados pelo computador receptor.Quanto mais bits puderem passar por esses fios e cabos por vez, mais rapidamente a internet funcionará.
A internet funciona por rede distribuída, ou seja, não existe um centro de controle central e não depende de nenhuma máquina individual, 
Há dois conceitos principais que são fundamentais para o funcionamento da internet: pacotes e protocolos.

    - Pacote :
    Um pacote de rede é um pequeno segmento de uma mensagem maior, contendo dados e um "cabeçalho" que fornece informações essenciais para o receptor. Os dados são divididos em pacotes menores, transformados em bits e enviados por dispositivos como roteadores e switches. Ao chegarem ao destino, os pacotes são remontados na ordem correta para exibir ou usar os dados.
    Esse processo é comparável ao envio da Estátua da Liberdade em partes da França para os EUA, onde foi remontada com instruções específicas. Enquanto a montagem da estátua foi demorada, a transmissão de dados pela internet é extremamente rápida, ocorrendo em milissegundos.
    A técnica usada é chamada de comutação de pacotes, permitindo que roteadores e switches processem pacotes independentemente, evitando que uma única conexão monopolize a rede. Sem essa técnica, a internet seria limitada a poucos usuários simultâneos, em vez do grande número atual.

    - Protocolos 
    Um protocolo é uma forma padronizada de realizar determinadas ações e formatar dados para que dois ou mais dispositivos sejam capazes de se comunicar entre si e de entender um ao outro.
    Existem protocolos para envio de pacotes entre dispositivos na mesma rede (Ethernet), para envio de pacotes de rede para rede (IP), para garantir que esses pacotes cheguem com sucesso e em ordem (TCP) e para formatação de dados para sites e aplicativos (HTTP). Além desses protocolos fundamentais, existem também protocolos para roteamento, testes e criptografia. E há alternativas aos protocolos listados acima para diferentes tipos de conteúdo - por exemplo, o streaming de vídeo frequentemente usa o protocolo UDP em vez do TCP.

    Como todos os computadores conectados à internet e a outros dispositivos podem interpretar e entender esses protocolos, a internet funciona independentemente de quem ou o que se conecta a ela.


Representação de dados 

Como aprendido em arquitetura de computadores, um computador não recebe os dados diretamente ele recebe os valores em bits que são representados com 0 ou 1, inclusive quando enviamos por exemplo uma letra  o computador recebe um conjunto de bits(byte) que representa essa letra, usando o código multibyte UTF-8.

    Grandeza das representações:
    > bit > byte > KB > MB > GB > TB > PB > EB...


Quais as etapas para a conseguir acessar um aplicação web na internet:

1. Consulta DNS: Quando seu navegador começou a carregar esta página web, provavelmente fez uma consulta DNS para descobrir o endereço de IP do site.
2. Handshake TCP: Seu navegador iniciou uma conexão com esse endereço de IP.
3. Handshake TLS: Seu navegador também configurou a criptografia entre um servidor web e seu dispositivo para que os invasores não possam ler os pacotes de dados que viajam entre esses dois endpoints.
4. Solicitação HTTP: Seu navegador solicitou o conteúdo que aparece nesta página web.
5. Resposta HTTP: O servidor transmitiu o conteúdo na forma de código HTML, CSS e JavaScript, dividido em uma série de pacotes de dados. Depois que seu dispositivo recebeu os pacotes e verificou que tinha recebido todos eles, seu navegador interpretou os códigos HTML, CSS e JavaScript contidos nos pacotes para renderizar este artigo sobre como a internet funciona. Todo o processo demorou apenas um segundo ou dois.



[Video](https://www.youtube.com/watch?v=nlO5hySqJFA)

- Como a Web funciona? ✨
Aplicação WEB trata-se de uma aplicação de software que roda na internet, em vez de funcionar com base em sistemas operacionais.
Assim, é um sistema com funcionalidades completas, que foi programado a partir de requisitos e dos princípios da engenharia de software. Contudo, seu grande diferencial é que ele é feito para funcionar na internet.


    Funcionamento
    Uma aplicação web funciona com base na infraestrutura da internet. 
    Primeiro ele vai pega a url que você digitou e enviar para um servidor DNS, esse servidor vai acessar o IP que referencia aquele site, então o site envia os pacotes para o usuário, por fim o usuário pode interagir com a plataforma enviando informações, alterando e salvando novos dados etc.
    Tudo isso representa interações que podem ser traduzidas em envio de requisições cliente-servidor.
- Protocolos ✨
    - [ ] IP
        IP - Protocolo da Internet um dos protocolos mais importantes da web,  Ele permite a elaboração e transporte dos pacotes de dados, porém sem assegurar a sua entrega.Quem garante que a entrega daqueles dados está indo pra o usuário correto.
        O destinatário da mensagem é determinado por meio dos campos de endereço IP (endereço do computador), máscara de sub rede (determina parte do endereço que se refere à rede) e o campo gateway estreita por padrão (permite saber qual o computador de destino, caso não esteja localizado na rede local).
    - [ ]  TCP / IP
        Trata-se do acrônimo de dois protocolos combinados são eles o TCP (Transmission Control Protocol — Protocolo de Controle de Transmissão) e IP (Internet Protocol — Protocolo de Internet).
        Juntos, são os responsáveis pela base de envio e recebimento de dados por toda a internet. Essa pilha de protocolos é dividida em 4 camadas:

            aplicação: usada para enviar e receber dados de outros programas pela internet. Nessa camada estão os protocolos HTTP, FTP e SMTP;
            transporte: responsável por transportar os arquivos dos pacotes recebidos da camada de aplicação. Eles são organizados e transformados em outros menores, que serão enviados à rede;
            rede: os arquivos empacotados na camada de transporte são recebidos e anexados ao IP da máquina que envia e recebe os dados. Em seguida, eles são enviados pela internet;
            interface: é a camada que executa o recebimento ou o envio de arquivos na web.
    - [ ]  HTTP/HTTPS
        O protocolo HTTP (Protocolo de Transferência de Hipertexto) - é usado para navegação em sites da internet. Funciona como uma conexão entre o cliente (browser) e o servidor (site ou domínio).O navegador envia um pedido de acesso a uma página, e o servidor retorna uma resposta de permissão de acesso. Junto com ela são enviados também os arquivos da página que o usuário deseja acessar.
        HTTPS( Protocolo de Transferência de Hipertexto Seguro) -funciona exatamente como o HTTP, porém, existe uma camada de proteção a mais. Isso significa que os sites que utilizam esse protocolo são de acesso seguro.
    - [ ]  SSH
        SSH (Secure Shell) é um dos protocolos específicos de segurança de troca de arquivos entre cliente e servidor. Funciona a partir de uma chave pública. Ela verifica e autentica se o servidor que o cliente deseja acessar é realmente legítimo.
    - [ ]  SSL / TLS
        O SSL (camada de portas de segurança) permite a comunicação segura entre os lados cliente e servidor de uma aplicação web, por meio de uma confirmação da identidade de um servidor e a verificação do seu nível de confiança.
        Ele age como uma subcamada nos protocolos de comunicação na internet (TCP/IP). Funciona com a autenticação das partes envolvidas na troca de informações.
- Browsers e como eles funcionam ✨
- DNS ✨
- VPN ✨