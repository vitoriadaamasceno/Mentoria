# Hands-on: Criando um Dockerfile

Criar um Dockerfile para construir uma imagem Docker a partir do zero.

## Objetivos

- Entender a estrutura básica de um Dockerfile.
- Criar um Dockerfile para uma aplicação simples.
- Aprender melhores práticas para otimização de imagens.

## Estrutura Básica de um Dockerfile

Um Dockerfile é um arquivo de texto que contém uma série de instruções que o Docker utiliza para construir uma imagem. 

### Instruções comuns:

- `FROM`: Define a imagem base
- `RUN`: Executa comandos durante a construção da imagem
- `COPY`: Copia arquivos ou diretórios para a imagem
- `CMD`: Define o comando padrão a ser executado quando um container é iniciado
- `EXPOSE`: Indica a porta que será exposta pelo container

## Exemplo Prático: Criando um Dockerfile para uma Aplicação Python com Flask

### Passo 1: Criar a Estrutura do Projeto

Crie um diretório e navegue até ele

```bash
mkdir my-flask-app
cd my-flask-app
```

### Passo 2: Criar o Arquivo `Dockerfile`

Crie um arquivo chamado `Dockerfile` no diretório criado anteriormente e adicione o seguinte conteúdo:

```Dockerfile
# usando a imagem base do python
FROM python

# definindo o diretório de trabalho
WORKDIR /usr/src/app

# copiando requirements.txt
# COPY requirements.txt ./
COPY requirements.txt requirements.txt

# instalando dependências
RUN pip install -r requirements.txt

# copiando o restante dos arquivos
# COPY . /usr/src/app
COPY . .

# expondo a porta 5000
EXPOSE 5000

# definindo variável de ambiente do Flask
ENV FLASK_APP=main.py

# comando padrão para iniciar a aplicação
CMD ["flask", "run", "--host=0.0.0.0"]

```

### Passo 3: Criar o Arquivo `main.py`

Crie um arquivo chamado `main.py` com o seguinte conteúdo:

```python
import logging

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    logging.info("Hello World")
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True)
```

### Passo 4: Criar o `requirements.txt`

Crie o `requirements.txt`:

```txt
Flask==3.0.2
```

### Passo 5: Construir a Imagem

```bash
docker build -t my-flask-app .
```

### Passo 6: Executar o Container

```bash
docker run --name <container-name> -p <host-port>:<container-port> <image>

docker run --name my-flask-app -p 5000:5000 my-flask-app
```

### Passo 7: Testar

Abra seu navegador e acesse `http://localhost:5000`.


