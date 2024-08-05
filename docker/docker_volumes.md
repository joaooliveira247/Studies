# Docker volumes

Docker volumes são uma maneira de persistir dados gerados e usados por contêineres Docker. Por padrão, os dados dentro de um contêiner são armazenados no sistema de arquivos do contêiner e são perdidos quando o contêiner é removido. Volumes permitem que você armazene dados de forma independente do ciclo de vida do contêiner, facilitando a persistência e o compartilhamento de dados entre diferentes contêineres.

Existem diferentes tipos de volumes em Docker:

1. Volumes gerenciados pelo Docker: Docker cria e gerencia esses volumes. Eles são armazenados em um local padrão no host e são ideais para a maioria dos casos de uso, pois Docker lida com a gestão dos dados.

2. Volumes bind mounts: Esses volumes são criados diretamente em um caminho especificado do sistema de arquivos do host. Eles oferecem mais controle sobre onde os dados são armazenados no host, mas também são mais propensos a problemas de segurança e permissões.

3. Volumes tmpfs: São armazenados na memória do sistema e não no sistema de arquivos do host. Eles são úteis para dados temporários que não precisam ser preservados após o término do contêiner.

## Bind mount

Docker Bind Mount é uma forma de montar um diretório ou arquivo do sistema de arquivos do host diretamente em um contêiner. Ao usar um bind mount, você especifica o caminho no host e o caminho onde ele deve ser montado dentro do contêiner. Isso permite que o contêiner acesse, leia e escreva diretamente nos arquivos e diretórios do host.

### Características dos Bind Mounts

1. Acesso direto aos dados do host: Diferente dos volumes gerenciados pelo Docker, que são armazenados em locais gerenciados pelo próprio Docker, os bind mounts utilizam diretórios e arquivos específicos do sistema de arquivos do host. Isso é útil quando você precisa que um contêiner acesse dados já presentes no sistema de arquivos do host ou compartilhe dados entre contêineres e o sistema do host.

2. Controle de permissões: Como os bind mounts usam o sistema de arquivos do host, eles herdam as permissões de arquivos e diretórios do host. Isso pode ser vantajoso para controlar o acesso aos dados, mas também requer atenção para evitar problemas de segurança e permissões inadequadas.

3. Performance: Bind mounts podem oferecer melhor desempenho em certos cenários, pois os dados não precisam ser copiados para um sistema de arquivos gerenciado por Docker.

4. Persistência de dados: Dados em bind mounts persistem além do ciclo de vida do contêiner, o que significa que eles são preservados mesmo se o contêiner for removido.

### Como usar Bind Mounts

Para usar um bind mount, você pode usar o comando docker run com a opção `-v` ou `--mount`. Por exemplo:

```bash
docker run -v /caminho/do/host:/caminho/no/container imagem
```

Neste exemplo, /caminho/do/host é o caminho no sistema de arquivos do host, e /caminho/no/container é o caminho onde o diretório ou arquivo será montado dentro do contêiner.

Exemplo prático

Se você deseja montar um diretório local chamado /data em um contêiner no caminho /app/data, você pode usar o seguinte comando:

```bash
docker run -v /data:/app/data imagem
```

Isso permitirá que o contêiner acesse diretamente os dados armazenados em /data no host, dentro do caminho /app/data no contêiner.

1. Montar um diretório do host em um contêiner

```bash
docker run --mount type=bind,source=/caminho/do/host,target=/caminho/no/container imagem
```

Neste exemplo:

`type=bind` especifica que é um bind mount.

`source=/caminho/do/host` é o caminho no sistema de arquivos do host que será montado.

`target=/caminho/no/container` é o caminho dentro do contêiner onde o diretório ou arquivo será acessível.

2. Montar um arquivo específico do host em um contêiner

```bash
docker run --mount type=bind,source=/caminho/do/host/arquivo.txt,target=/caminho/no/container/arquivo.txt,readonly imagem
```

Neste exemplo:

`source=/caminho/do/host/arquivo.txt` é o caminho do arquivo no host.

`target=/caminho/no/container/arquivo.txt` é o caminho dentro do contêiner.

`readonly` é uma opção adicional que monta o arquivo como somente leitura no contêiner.

3. Usar um bind mount para compartilhar logs do host com um contêiner

```bash
docker run --mount type=bind,source=/var/logs,no-volume-mode,target=/app/logs imagem
```

Neste exemplo:

`source=/var/logs` especifica o diretório de logs no host.

`target=/app/logs` é onde os logs estarão acessíveis dentro do contêiner.

Esses exemplos mostram como usar a opção --mount para configurar bind mounts, permitindo que diretórios e arquivos do host sejam acessíveis dentro de contêineres Docker

## Volumes

Docker volumes são uma forma de persistir dados gerados e usados pelos contêineres Docker. Eles permitem que você armazene dados fora do ciclo de vida de um contêiner, garantindo que esses dados não sejam perdidos quando o contêiner é removido. Existem três principais tipos de armazenamento em Docker:

Volumes: São gerenciados pelo Docker e armazenados na máquina host, mas em um local separado do sistema de arquivos do contêiner. Eles são a forma mais recomendada de persistir dados, pois são fáceis de usar e podem ser compartilhados entre contêineres.

### Criando e usando volumes
Para criar um volume:

bash
Copy code
docker volume create nome_do_volume
Para usar um volume em um contêiner:

```bash
docker run -d -v nome_do_volume:/caminho_no_container imagem
```

Exemplos

- Criar um volume e usar em um contêiner:

```bash
docker volume create meus_dados
docker run -d -v meus_dados:/var/lib/mysql mysql
```

Montar um diretório específico do host (bind mount):

```bash
docker run -d -v /caminho/no/host:/caminho/no/container nginx
```

Mostra especificações do volume

```bash
docker volume inspect volume_name
```


### Outras formas

certifique-se de verificar onde a imagem geralmente monta os dados.

```bash
docker run -d --mount type=volume,source=meu_volume,target=/app/data nginx

```

### Usando a instrução VOLUME no Dockerfile

A sintaxe básica para VOLUME no Dockerfile é a seguinte:

```dockerfile
VOLUME ["/caminho/no/container"]
```

Você pode especificar um ou mais diretórios que serão montados como volumes. Aqui estão alguns exemplos:

Exemplo Básico

```dockerfile
# Usando a imagem base do nginx
FROM nginx:latest

# Definindo um volume para o diretório /app
VOLUME ["/app"]

# Copiando arquivos de configuração para o contêiner
COPY . /app

# Definindo o diretório de trabalho
WORKDIR /app
```

Neste exemplo:

VOLUME ["/app"] define que o diretório /app dentro do contêiner será um volume.
Os dados em /app serão persistidos fora do ciclo de vida do contêiner.

### Removendo todos os volumes

```bash
docker volume prune --all
```

## TMPFS

temporary filesystem) é uma forma de montar um sistema de arquivos em memória no Docker, que é útil para armazenar dados temporários que não precisam ser persistidos após a reinicialização do contêiner. Você pode usar tmpfs para melhorar o desempenho ao evitar a escrita no disco e para garantir que os dados não sejam mantidos após o ciclo de vida do contêiner.

Embora você não possa definir um tmpfs diretamente no Dockerfile, você pode configurar um tmpfs mount ao iniciar um contêiner usando a linha de comando docker run ou em um arquivo de configuração do Docker Compose.

```bash
docker run -d --mount type=tmpfs,target=/app,tmpfs-size=100m,tmpfs-mode=1777 nginx
```
