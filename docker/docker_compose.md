# Docker compose

Docker Compose é uma ferramenta que facilita o gerenciamento de aplicações Docker compostas por múltiplos contêineres. Ele permite definir e orquestrar a execução de contêineres usando um arquivo YAML, geralmente chamado de docker-compose.yml. Neste arquivo, você especifica os serviços que compõem a sua aplicação, as imagens Docker a serem usadas, as redes, volumes, e outras configurações necessárias.

## Principais conceitos:

`Serviços`: Cada serviço no docker-compose.yml representa um contêiner Docker. Por exemplo, você pode ter um serviço para o banco de dados, outro para o backend, e outro para o frontend.

`Volumes`: Permitem persistir dados entre execuções de contêineres, mesmo que o contêiner seja destruído e recriado.

`Redes`: Facilitam a comunicação entre os contêineres, permitindo que eles se encontrem por nomes de serviço.

`Comandos`: Você pode usar comandos como docker-compose up para iniciar todos os serviços definidos no arquivo docker-compose.yml, ou docker-compose down para parar e remover os contêineres.

```yaml
version: '3'
services:
  web:
    image: my-web-app
    ports:
      - "8080:80"
    depends_on:
      - db
  db:
    image: postgres
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
```

Neste exemplo, temos dois serviços: web e db. O serviço web depende do db e expõe a porta 8080 no host, mapeada para a porta 80 no contêiner. O serviço db usa a imagem do PostgreSQL e define variáveis de ambiente para configurar o banco de dados.

### Build

Exemplo de um Dockerfile:

```Dockerfile
FROM golang:1.20-alpine

WORKDIR /app

COPY . .

RUN go mod download
RUN go build -o main .

CMD ["./main"]
```

Configurar o docker-compose.yml: Crie um arquivo chamado docker-compose.yml na raiz do seu projeto. Este arquivo definirá os serviços, incluindo o contexto de construção (build) para cada serviço.

Exemplo de um docker-compose.yml:

```yaml
version: '3.8'

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "8080:8080"
    volumes:
      - .:/app
    environment:
      - PORT=8080
```

`context`: Especifica o contexto de build (geralmente o diretório contendo seu Dockerfile).

`dockerfile`: Especifica qual Dockerfile usar (o padrão é Dockerfile se não for especificado).

`ports`: Mapeia a porta 8080 da sua máquina local para a porta 8080 no contêiner.

`volumes`: Monta seu diretório de projeto no contêiner, permitindo que alterações no código sejam refletidas imediatamente.

Construir e Executar com Docker Compose: Use os comandos do Docker Compose para construir a imagem e executar o contêiner.

```bash
# Construir a imagem Docker
docker-compose build

# Iniciar o contêiner
docker-compose up
```

`docker-compose build`: Constrói a imagem com base nas instruções no Dockerfile e no docker-compose.yml.

`docker-compose up`: Inicia o contêiner usando a imagem construída. Ele também reconstrói a imagem automaticamente se algum arquivo do contexto de build tiver sido alterado desde a última construção.

Parar e Remover Contêineres: Quando você terminar, pode parar e remover os contêineres com:

```bash
docker-compose down
```

Estrutura de Projeto Exemplo
Seu projeto pode ter a seguinte estrutura:

```go
meu-app-go/
│
├── Dockerfile
├── docker-compose.yml
├── main.go
└── go.mod
```

Explicação

`Dockerfile`: Contém as instruções para construir sua aplicação Go.

`docker-compose.yml`: Orquestra a construção e execução da sua aplicação, facilitando o gerenciamento de setups com múltiplos contêineres.

`main.go`: O código da sua aplicação Go.

`go.mod`: O arquivo de módulos Go.

Construindo e Executando com Mudanças
Sempre que você fizer alterações no Dockerfile ou nos arquivos envolvidos no processo de construção, pode simplesmente rodar:

```bash
docker-compose up --build
```