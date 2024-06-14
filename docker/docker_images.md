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
docker run -it b9390dd1ea18 bash
```