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

## Build

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

## Volumes

Volumes no Docker Compose são usados para persistir dados gerados e utilizados por contêineres. Eles permitem que os dados sejam salvos em locais que não são removidos quando o contêiner é destruído, facilitando o armazenamento persistente e o compartilhamento de dados entre múltiplos contêineres.

### Tipos de Volumes no Docker Compose

#### Named Volumes (Volumes Nomeados):

Os volumes nomeados são gerenciados pelo Docker e são criados fora do ciclo de vida dos contêineres. Eles são reutilizáveis entre diferentes contêineres e são úteis para persistir dados entre reinicializações.
Bind Mounts:

Um bind mount mapeia um diretório ou arquivo específico do host (sua máquina) para um diretório no contêiner. Ele é útil para desenvolvimento, pois permite que você compartilhe seu código-fonte com o contêiner.

Exemplo de Configuração de Volumes no Docker Compose

1. Named Volumes
Aqui está um exemplo de como definir e usar volumes nomeados em um arquivo `docker-compose.yml`:

```yaml
version: '3.8'

services:
  db:
    image: postgres
    volumes:
      - db-data:/var/lib/postgresql/data
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password

volumes:
  db-data:
```

`db-data:/var/lib/postgresql/data`: Aqui, db-data é um volume nomeado que é montado no caminho /var/lib/postgresql/data dentro do contêiner.

`volumes:`: A seção volumes no final do arquivo define o volume `db-data`, que o Docker gerencia.

2. Bind Mounts

```yaml
version: '3.8'

services:
  app:
    image: my-web-app
    volumes:
      - ./src:/app/src
    ports:
      - "8080:80"
```

`./src:/app/src`: Este bind mount mapeia o diretório src do host (onde o código-fonte está localizado) para o diretório /app/src dentro do contêiner. Isso permite que as mudanças feitas no código local sejam refletidas imediatamente no contêiner.

3. Usando Ambos em um Projeto
Você pode combinar named volumes e bind mounts em um mesmo projeto:

```yaml
version: '3.8'

services:
  web:
    image: my-web-app
    volumes:
      - ./src:/app/src    # Bind mount para código-fonte
      - app-data:/app/data # Volume nomeado para dados persistentes
    ports:
      - "8080:80"

volumes:
  app-data:
```

## Restart

O Docker Compose oferece várias opções para reiniciar automaticamente os contêineres em caso de falha, ou para garantir que eles sejam reiniciados quando o sistema for reiniciado. Isso é feito através da opção restart no arquivo docker-compose.yml.

### Opções de Reinício (restart)

`no`:

Não reinicia automaticamente o contêiner. Este é o comportamento padrão.

`always`:

Sempre reinicia o contêiner, independentemente do código de saída. Ele será reiniciado automaticamente se for interrompido ou se o Docker for reiniciado.

`on-failure`:

Reinicia o contêiner apenas se ele sair com um código de falha diferente de zero. Você pode especificar o número máximo de tentativas de reinício com on-failure:N.

`unless-stopped`:

Similar ao always, exceto que o contêiner não será reiniciado se ele foi parado manualmente (com docker stop) ou se o Docker não for reiniciado.
Exemplo de Configuração restart no docker-compose.yml

Aqui está um exemplo de como usar a opção restart no docker-compose.yml:

```yaml
version: '3.8'

services:
  web:
    image: my-web-app
    ports:
      - "8080:80"
    restart: always

  db:
    image: postgres
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    restart: on-failure:5
```

`restart: always`: O serviço web será reiniciado sempre que parar, mesmo que seja devido a uma falha ou reinicialização do Docker.

`restart: on-failure:5`: O serviço db será reiniciado até 5 vezes se falhar com um código de erro diferente de zero.
Reinício Manual
Além da configuração automática, você também pode reiniciar contêineres manualmente com os seguintes comandos:

### Reiniciar todos os serviços:

```bash
docker-compose restart
```

### Reiniciar um serviço específico:

```bash
docker-compose restart <service_name>
```

## env_file

A opção env_file no Docker Compose permite que você carregue variáveis de ambiente a partir de um arquivo .env para seus contêineres. Isso é útil para manter suas configurações, como senhas, tokens ou outras variáveis de ambiente, fora do código-fonte, facilitando a configuração do ambiente de execução.

Como Usar env_file no Docker Compose
Criar um Arquivo .env:

Crie um arquivo .env no diretório do seu projeto, ou em um local onde você deseja armazenar suas variáveis de ambiente.
Exemplo de um arquivo .env:

```dotenv
DATABASE_URL=postgres://user:password@db:5432/mydatabase
API_KEY=your_api_key_here
APP_ENV=production
```

Configurar o docker-compose.yml:

No arquivo docker-compose.yml, utilize a opção env_file para especificar o arquivo que contém as variáveis de ambiente.
Exemplo de um docker-compose.yml utilizando env_file:

```yaml
version: '3.8'

services:
  app:
    image: my-web-app
    env_file:
      - .env
    ports:
      - "8080:80"
  
  db:
    image: postgres
    env_file:
      - .env
    volumes:
      - db-data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

volumes:
  db-data:
```

`env_file`: - .env: Este comando informa ao Docker Compose para carregar as variáveis de ambiente do arquivo .env e passá-las para o contêiner.

Você pode especificar mais de um arquivo env_file, se necessário, listando-os como uma matriz (array).

### Como Funciona

- Precedência: Se uma variável de ambiente estiver definida tanto no env_file quanto diretamente no docker-compose.yml (na seção environment), o valor definido diretamente no docker-compose.yml terá precedência.

- Uso das Variáveis: As variáveis definidas no env_file são acessíveis dentro do contêiner como variáveis de ambiente. Por exemplo, no contêiner, você pode acessar DATABASE_URL e outras variáveis definidas.

## Networks

No Docker Compose, a configuração de networks permite que você gerencie como os contêineres se conectam uns aos outros e a outros recursos de rede. Com networks, você pode definir redes personalizadas, controlar o isolamento entre os serviços, e conectar contêineres a redes externas.

### Tipos de Redes no Docker Compose

#### Bridge (Ponte):

É o tipo de rede padrão no Docker. Contêineres na mesma rede bridge podem se comunicar entre si usando seus nomes de serviço ou endereços IP. Este tipo de rede é isolado do host e de outras redes a menos que explicitamente configurado para permitir acesso.

#### Host:

No modo host, o contêiner compartilha a pilha de rede do host, ou seja, ele se conecta diretamente à rede do host sem um namespace de rede isolado. Isso é útil para serviços que precisam de desempenho de rede elevado.

#### None:

O contêiner não recebe uma interface de rede. Isso é útil para contêineres que não precisam de acesso à rede.

#### Overlay:

Usado em ambientes Docker Swarm, permite que contêineres em diferentes hosts Docker se comuniquem de maneira segura. Não é normalmente usado em configurações simples de Docker Compose.
Definindo Redes no Docker Compose
1. Criando Redes Personalizadas
Você pode definir redes personalizadas no arquivo docker-compose.yml para controlar como os serviços se comunicam.

Exemplo básico:

```yaml
version: '3.8'

services:
  web:
    image: my-web-app
    networks:
      - frontend
    ports:
      - "8080:80"

  db:
    image: postgres
    networks:
      - backend

networks:
  frontend:
  backend:
```

`networks:`: A seção networks no final do arquivo define as redes personalizadas frontend e backend.

`networks: - frontend`: Dentro do serviço web, isso conecta o contêiner à rede frontend.

`networks: - backend`: Conecta o contêiner db à rede backend.

2. Conectando Múltiplas Redes
Um serviço pode ser conectado a várias redes, permitindo que ele se comunique com diferentes grupos de contêineres.

Exemplo:

```yaml
version: '3.8'

services:
  app:
    image: my-app
    networks:
      - frontend
      - backend

  web:
    image: nginx
    networks:
      - frontend

  db:
    image: postgres
    networks:
      - backend

networks:
  frontend:
  backend:
```

Neste exemplo:

O serviço app está conectado a ambas as redes frontend e backend, permitindo que ele se comunique com ambos os serviços web e db.

O serviço web só pode se comunicar com app via frontend.

O serviço db só pode se comunicar com app via backend.

3. Configurando Redes Externas
Você também pode conectar seus contêineres a redes que foram criadas fora do escopo do Docker Compose.

Exemplo:

```yaml
version: '3.8'

services:
  app:
    image: my-app
    networks:
      - external_network

networks:
  external_network:
    external: true
```

Aqui, external_network refere-se a uma rede já existente no Docker. Se a rede não existir, o Docker Compose não a criará automaticamente, e o comando falhará.

