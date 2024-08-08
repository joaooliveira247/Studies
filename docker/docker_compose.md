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