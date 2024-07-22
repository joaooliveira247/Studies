# Docker Images

## Executando imagem [alphine-nodejs](https://hub.docker.com/_/node)

`Dockerfile`

```dockerfile
FROM node:current-alpine3.20
RUN mkdir -p /opt/app-nodejs
COPY server.js /opt/app-nodejs
WORKDIR /opt/app-nodejs/
CMD node server.js
```

`server.js`

```js
// server.mjs
import { createServer } from 'node:http';

const server = createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Hello World!\n');
});

// starts a simple http server locally on port 3000
server.listen(3000, '0.0.0.0', () => {
  console.log('Listening on 127.0.0.1:3000');
});

// run with `node server.mjs`

```

|Comando|Descrição|
|:---:|:---:|
|FROM <image_name>| Define de qual lugar será obtido a imagem para criação do container|
|RUN \<command>|usado para definir algo na construção da imagem|
|COPY \<path> <container_path>|copia arquivo ou pasta para dentro do container|
|WORKDIR \<container_path>|define um diretorio padrão para trabalho|
|CMD \<command>|usado definir um comando que vai ser executado quando a imagem for carregada, somente 1 por dockerfile|

---

### Criando o container

`docker build -t <container_tag> <dockerfile_path>`

`ex`

```shell
docker build -t app-nodejs .
```

---

### Executando o container

`docker run -p <container_port:local_port> <image_name>`

`ex`

```shell
docker run -p 3000:3000 app-nodejs
```

## Images tags

Uma tag Docker é um rótulo aplicado a uma imagem Docker, ajudando a identificar versões ou configurações específicas da imagem

`docker build -t <tag> <path>`

`docker tag <iamge_id> <namespace/repository:version>`

`ex`

```shell
docker tag bc6434c28e9a prod/app-nodejs:1.0.0
```

## Inspect

Retornar informações de baixo nível sobre objetos Docker

`docker inspect <image_id>`

`ex`

```shell
docker inspect f9fc7e669876
```

## "Entrando" dentro de um container

`docker run -it <image> <shell>`

`ex`

```shell
docker run -it b9390dd1ea18 /bin/sh
```

## RUN - Dockerfile

Executa comando no shell do container

```Dockerfile
FROM alpine:latest
RUN apk add --no-cache nodejs
RUN apk add --no-cache npm
```

*Obs:* apk é o gerenciador de pacotes do alphine

### Multiline RUN

```Dockerfile
RUN command_1 && \
    command_2 && \
    command_3
```

```Dockerfile
RUN command_1 \
    && command_2 \
    && command_3
```

```Dockerfile
RUN <<<EOF
    command_1
    command_2
    command_3
EOF
```
## LABEL - Dockerfile

adiciona labels/informaçãos aos metadados do container

use o comando 

`docker image inspect <container_id>`

a flag `--format="value"` define um padrão de retorno o value usa placeholders para definir a resposta, uma padrão bem parecido com jinja.

### label simples

```Dockerfile
FROM alpine:latest
LABEL <key>=<value>
```

### multiline labels

```Dockerfile
FROM apine:latest
LABEL <key>=<value> <key>=<value>
```

```Dockerfile
FROM apine:latest
LABEL <key>=<value> \
      <key>=<value> \
      <key>=<value>
```

`ex:`

```Dockerfile
docker image inspect --format="{{ json .Config.Labels }}" 10d7fb41183a
```

## ENV - Dockerfile

```Dockerfile
FROM alpine:latest
ENV FRONT_PROD="https://meuapp.com.br"
```

```Dockerfile
FROM alpine:latest
ENV FRONT_PROD "https://meuapp.com.br"
```

### multiline env

```Dockerfile
FROM alpine:latest
ENV FRONT_PROD="https://meuapp.com.br" \
    BACK_PROD="https://meuapp.com.br:3000"
```

### usando env como var envs no dockerfile

```Dockerfile
FROM alpine:latest
ENV FRONT_PROD="https://meuapp.com.br" \
    BACK_PROD="https://meuapp.com.br:3000" \
    APP_NAME="someApp"
LABEL app_name=${APP_NAME}
```

## ARG - Dockerfile

`ARG` é uma instrução que define variáveis de build (build-time variables) que podem ser passadas para o processo de construção da imagem Docker. Essas variáveis podem ser usadas para personalizar a construção da imagem sem modificar diretamente o Dockerfile.

```Dockerfile
ARG ALPINE_VERSION
FROM alpine:${ALPINE_VERSION}
```

`docker build --build-arg ALPINE_VERSION=latest -t <tag> <path>`

você também pode atribuir valores padrões caso o argumento não sejá passado.

`ARG ALPINE_VERSION=3.17`

## USER - Dockerfile

Define o usuário para executar as instruções seguintes e o processo principal do contêiner.

por padrão o usuário é o root

```Dockerfile
FROM alpine:latest
RUN adduser -D <username>
USER <username>
```

## CMD - Dockerfile

Especifica o comando que será executado quando um contêiner é iniciado a partir da imagem. Só pode haver uma instrução CMD por Dockerfile.

```Dockerfile
FROM alpine:latest
CMD ["/bin/sh", "-c", "echo something"]
```

você pode passar o cmd na hora do build também.

`docker build <image> <cmd>`

## ADD - Dockerfile

Copia arquivos e diretórios do host para o sistema de arquivos da imagem. `ADD` também pode extrair arquivos tar e baixar arquivos a partir de URLs.

cada `ADD` gera uma camada e isso diminui a performace na hora do build

```Dockerfile
FROM alpine:latest
RUN adduser -D <username>
USER <username>
ADD <path> <container_path>
ADD url <container_path>
ADD --chown=<username>:<group> <path> <container_path>
```

caso o alvo de ADD sejá com path parecido use

```Dockerfile
FROM alpine:latest
RUN adduser -D <username>
USER <username>
ADD --chown=<username>:<group> ./<pattern>* <container_path>
ADD --chown=<username>:<group> ./<pattern>?<pattern> <container_path>
```

`*` - 1 ou n padrões

`?` - exatamente 1 padrão

## COPY - Dockerfile

Mesma coisa que o `ADD`, `COPY` copia somente do `host` para `container`, sendo semanticamente mais limpo nesse processo.

```Dockerfile
FROM alpine:latest
COPY <path> <container_path>
```

você pode adicionar as flags de permissão provenientes do OS.

`--chown=<user>:<perm>` ou `chmod=777`

### multi copy

```Dockerfile
FROM alpine:latest
COPY <path> <path> <path> <container_path>
```

```Dockerfile
FROM alpine:latest
COPY . <container_path>
```

`.` copia tudo no mesmo diretorio q o dockerfile

## ENTRYPOINT - Dockerfile

O ENTRYPOINT no Dockerfile é uma instrução usada para configurar o container de forma que ele execute um comando específico quando for iniciado. Ao contrário da instrução CMD, que pode ser substituída ao passar argumentos na linha de comando durante a execução do container, o ENTRYPOINT define um comando fixo que sempre será executado. Isso é útil para containers que devem executar uma aplicação ou script específico como seu processo principal.

`CMD`: Pode ser substituído ao passar um comando na linha de comando (docker run meu_container comando_substituto).

`ENTRYPOINT`: Não pode ser substituído dessa forma, mas você pode adicionar argumentos ao comando definido pelo ENTRYPOINT.

```Dockerfile
FROM alpine:latest
ENTRYPOINT ["python", "file.py"] 
```

`docker run --entrypoint <command> <container_id> <command_arg>`

### ENTRYPOINT executando shell script

`dockerfile-entrypoint.sh`

```shell
#!/bin/bash

echo "Load container"

for i in 1 2 3 4 5; do
    echo "count: $i"
done

echo "service in exec"

sleep 5
```

`Dockerfile`

```Dockerfile
FROM alpine:latest
COPY ./dockerfile-entrypoint.sh /start/dockerfile-entrypoint.sh
ENTRYPOINT ["/start/dockerfile-entrypoint.sh"]
```

## WORKDIR - Dockerfile

O comando `WORKDIR` em um Dockerfile é utilizado para definir o diretório de trabalho para as instruções subsequentes dentro desse Dockerfile. Isso é fundamental para organizar a estrutura de arquivos e garantir que comandos sejam executados no contexto correto dentro do contêiner.

```Dockerfile
FROM alpine:latest
RUN mkdir app
WORKDIR app/
```

## EXPOSE - Dockerfile

O comando EXPOSE no Dockerfile é usado para documentar a intenção de expor uma porta ou várias portas do contêiner para permitir a comunicação com o exterior. Ele não realmente "abre" as portas, mas serve como uma indicação para outras pessoas que usam a imagem ou para ferramentas automatizadas que as portas especificadas são usadas pelo contêiner.

```Dockerfile
FROM alpine:lates
EXPOSE 3000/tcp
EXPOSE 3000/udp
```

`docker run -P`

Pega como base oque estava no `EXPOSE`, mas gera automaticamente o bind no host.


## `Docker image history`

exibe o histórico de uma imagem Docker, mostrando as camadas (layers) que compõem a imagem e informações sobre cada camada, como o comando que foi executado para criar a camada, o autor, a data de criação, o tamanho da camada, entre outros detalhes. Esse comando é útil para entender como uma imagem foi construída e para depurar problemas relacionados à construção de imagens Docker.

`docker image history <image>`

## Layers (Camadas)

Uma imagem Docker é composta por uma série de camadas. Cada instrução no Dockerfile (como RUN, COPY, ADD, etc.) cria uma nova camada na imagem. Essas camadas são empilhadas uma sobre a outra para formar a imagem final. As camadas são fundamentais para o funcionamento eficiente do Docker, pois permitem a reutilização de partes da imagem.

Por exemplo, considere o seguinte Dockerfile:

```Dockerfile
dockerfile
Copy code
FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y python3
COPY . /app
CMD ["python3", "/app/app.py"]
```

Este Dockerfile geraria uma imagem com várias camadas:

- A camada base a partir da imagem ubuntu:latest.

- Uma camada criada pela instrução RUN apt-get update.

- Uma camada criada pela instrução RUN apt-get install -y python3.

- Uma camada criada pela instrução COPY . /app.

- A camada final que define o comando CMD ["python3", "/app/app.py"].

## Cache Layers (Camadas de Cache)

Docker utiliza um mecanismo de cache para acelerar o processo de construção de imagens. Quando você constrói uma imagem, Docker armazena em cache cada camada criada. Se você modificar o Dockerfile e reconstruir a imagem, Docker tentará reutilizar as camadas em cache sempre que possível. Isso é chamado de cache layer.

Por exemplo, se você modificar apenas a última instrução CMD no Dockerfile acima e reconstruir a imagem, Docker reutilizará as camadas em cache para as instruções anteriores (FROM, RUN apt-get update, RUN apt-get install -y python3, COPY . /app), e apenas reconstruirá a camada modificada. Isso acelera significativamente o processo de construção, pois evita a recompilação de camadas que não foram alteradas.

No entanto, é importante entender como o Docker determina se uma camada em cache pode ser reutilizada:

1. Instruções FROM: Se a imagem base mudou, todas as camadas seguintes serão invalidadas.

2. Instruções RUN, COPY, ADD: Docker verifica o comando e os arquivos envolvidos. Se os comandos ou arquivos mudaram, a camada será reconstruída e as camadas subsequentes também.

3. Instruções ENV, EXPOSE, VOLUME, etc.: Mudanças nestas instruções invalidarão as camadas que as seguem.
Exemplo de Uso do Cache
Considere este Dockerfile modificado:

```Dockerfile
Copy code
FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y python3
COPY . /app
CMD ["python3", "/app/new_app.py"]  # Modificamos o CMD
```

Ao reconstruir a imagem, Docker usará as camadas em cache para as instruções FROM, RUN apt-get update, RUN apt-get install -y python3, e COPY . /app, e apenas reconstruirá a camada CMD.

Forçando a Não Utilização do Cache
Se por algum motivo você precisar forçar a reconstrução de todas as camadas, você pode usar a opção --no-cache:


`docker build --no-cache -t my-image`

Isso desabilitará o uso do cache e garantirá que todas as camadas sejam reconstruídas do zero.

## Instruções que geram camadas

|Geram|Não Geram|
|:---:|:---:|
|FROM|LABEL|
|RUN|ENV|
|ADD|ARG|
|COPY|USER|
|WORKDIR|CMD|
|VOLUME|ENTRYPOINT|
||EXPOSE|

## Herança

No Docker, o conceito de "herança" pode ser entendido de forma semelhante à herança em programação orientada a objetos, mas aplicado a imagens Docker. Isso é realizado através do uso de arquivos Dockerfile, que especificam como construir uma imagem a partir de outra imagem base. Aqui está uma explicação detalhada:

Dockerfile
Um Dockerfile é um script de texto que contém uma série de instruções para construir uma imagem Docker. A instrução `FROM` no Dockerfile é usada para especificar a imagem base da qual a nova imagem será construída. Esse é o principal mecanismo de "herança" em Docker.

Exemplo
Considere o seguinte exemplo de Dockerfile:

```Dockerfile
# Especifica a imagem base
FROM python:3.9-slim

# Configura o diretório de trabalho
WORKDIR /app

# Copia os arquivos necessários para o contêiner
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

# Define o comando padrão a ser executado quando o contêiner é iniciado
CMD ["python", "app.py"]
```

Neste exemplo:

- A instrução FROM python:3.9-slim indica que a imagem base é python:3.9-slim. Esta imagem base já contém o Python 3.9 instalado.

- As instruções seguintes (WORKDIR, COPY, RUN e CMD) são usadas para adicionar funcionalidades adicionais à imagem base, como instalar dependências e copiar arquivos.

Herança em Ação

A herança no Docker é poderosa porque permite reutilizar imagens existentes como base para construir novas imagens, promovendo a reutilização e a modularidade. Por exemplo, você pode ter uma imagem base comum para todas as suas aplicações Python, e diferentes Dockerfiles que herdam dessa imagem base, adicionando apenas as dependências e código específicos de cada aplicação.

Vantagens da Herança no Docker

- Reutilização de Código: Reutilizar imagens base evita a duplicação de esforços e promove a consistência.

- Manutenção Facilitada: Atualizar a imagem base automaticamente propaga as atualizações para todas as imagens que herdam dela.

- Eficiência: As imagens Docker são construídas em camadas, o que significa que partes da imagem que não mudaram são reutilizadas, economizando tempo e espaço.