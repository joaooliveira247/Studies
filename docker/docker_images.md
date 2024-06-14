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

`docker build -t <container_name> <dockerfile_path>`

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