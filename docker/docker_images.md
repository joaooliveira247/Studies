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
