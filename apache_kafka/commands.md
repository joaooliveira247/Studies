# Kafka CLI commands

### `dir kafka/bin/`

## `kafka-topics.sh`

Cria, exclui, altera ou exibe informações de um tópico.

`flags`

|`flag`|Descrição|
|:---:|:---:|
|`--topic`|Nome do tópico|
|`--bootstrap-server`|Servidor Kafka para conectar|
|`--partitions`|Número de partições que o Tópico deve ter|
|`--replication-factor`|Fator de Replicação do tóppico(deve ser menor ou igual ao número de brokers)|
|`--create`|Cria um tópico|
|`--alter`|Altera o número de partições, replicas e outras configs|
|`--delete`|Deleta um tópico|
|`--describe`|Mostra detalhes do tópico|
|`--if-not-exists`|Só altera o tópico se ele não existir|
|`--list`|Lista todos os tópicos|

### Exemplos

#### Lista os tópicos existentes

```bash
./kafka-topics.sh --bootstrap-server 127.0.0.1:9092 --list 
```

#### Cria um novo tópico com 3 particões e 1 fator de replicação

```bash
./kafka-topics.sh --bootstrap-server 127.0.0.1:9092 --topic newtopic --create --partitions 3 --replication-factor 1
```

#### Lista os tópicos existentes

```bash
./kafka-topics.sh --bootstrap-server 127.0.0.1:9092 --list 
```

#### Mostra a descrição de um tópico

```bash
./kafka-topics.sh --bootstrap-server 127.0.0.1:9092 --topic newtopic --describe
```

#### Alterar partições

```bash
./kafka-topics.sh --bootstrap-server 127.0.0.1:9092 --topic novotopico --alter --partitions 4
```

#### Deleta um tópico

```bash
./kafka-topics.sh --bootstrap-server 127.0.0.1:9092 --topic novotopico --delete
```

## `kafka-console-producer.sh`

`flags`

|`flag`|Descrição|
|:---:|:---:|
|`--topic`|Nome do tópico|
|`--bootstrap-server`|Servidor Kafka para conectar|
|`--sync`|Define que as mensagens enviadas de forma sícrona ao broker|
|`--request-required-acks`|Confirmação requerida pelo producer. (Default=1)|
|`--message-send-max-retries`|Número máximo de tentativas de envio de mensagem. (Default=3)|

### Exemplos

#### Cria um tópico

```bash
./kafka-topics.sh --bootstrap-server 127.0.0.1:9092 --topic mensagens --create --partitions 3 --replication-factor 1
```

#### Console producer

```bash
./kafka-console-producer.sh --bootstrap-server 127.0.0.1:9092  --topic mensagens
```

#### Envia mensagem para topico não existente

```bash
./kafka-console-producer.sh --bootstrap-server 127.0.0.1:9092  --topic novasmensagens
```

#### lista os topicos para confirmar a criação

```bash
./kafka-topics.sh --bootstrap-server 127.0.0.1:9092 --list
```

## `kafka-console-producer.sh`

`flags`

|`flag`|Descrição|
|:---:|:---:|
|`--topic`|Nome do tópico|
|`--bootstrap-server`|Servidor Kafka para conectar|
|`--from-beginning`|Lê do inicio do tópico se ainda não houve uma leitura|
|`--group`|O grupo de consumo|
|`--isolation-level`|read_committed para ler mensagens confirmadas/read_uncommitted para ler todas mensagens(default)|
|`--offset`|offset a partir de qual se quer ler as mensagens. Pode também ser: `earliest`: desde o inicio/`latest`do fim(default)|
|`--partition`|Partição para ler as mensagens. Inicia do fim, a não ser que o `offset` sejá definido|

### Exemplos

#### Consumir do inicio

```bash
./kafka-console-consumer --bootstrap-server 127.0.0.1:9092 --topic mensagens --from-beginning
```

#### Producer

```bash
./kafka-console-producer.sh --bootstrap-server 127.0.0.1:9092  --topic mensagens
```

#### Consumir com off set

```bash
./kafka-console-consumer --bootstrap-server 127.0.0.1:9092 --topic mensagens --partions 0 --offset 2
```

```bash
./kafka-console-consumer --bootstrap-server 127.0.0.1:9092 --topic mensagens --partions 1 --offset 2
```

```bash
./kafka-console-consumer --bootstrap-server 127.0.0.1:9092 --topic mensagens --partions 2 --offset 2
```

#### Max messagens 

```bash
./kafka-console-consumer --bootstrap-server 127.0.0.1:9092 --topic mensagens --partions 2 --offset 2 --max-messagens 1
```

#### consumir de partições

```bash
./kafka-console-consumer --bootstrap-server 127.0.0.1:9092 --topic mensagens --partions 0
```

```bash
./kafka-console-consumer --bootstrap-server 127.0.0.1:9092 --topic mensagens --partions 1
```

```bash
./kafka-console-consumer --bootstrap-server 127.0.0.1:9092 --topic mensagens --partions 2
```

## `kafka-consumer-groups.sh`

`flags`

|`flag`|Descrição|
|:---:|:---:|
|`--topic`|Nome do tópico|
|`--bootstrap-server`|Servidor Kafka para conectar|
|`--describe`|Mostra detalhes do tópico|
|`--list`|Lista todos os tópicos|
|`--group`|Nome do grupo|
|`--reset-offsets`|Reseta offsets do tópico|

### Exemplos

#### Cria um consumidor com um grupo

```bash
./kafka-console-consumer.sh --bootstrap-server 127.0.0.1:9092 --topic mensagens --group consumidores
```


#### Cria outro consumidor com o mesmo grupo

```bash
./kafka-console-consumer.sh --bootstrap-server 127.0.0.1:9092 --topic mensagens --group consumidores
```


#### Cria um consumidor do mesmo topico mas de outro grupo

```bash
./kafka-console-consumer.sh --bootstrap-server 127.0.0.1:9092 --topic mensagens --group novosconsumidores
```

#### Mostra consumers groups

```bash
./kafka-consumer-groups.sh --bootstrap-server localhost:9092 --list
```

#### Descrever grupos

```bash
kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group consumidores
```

#### Abre um novo consumidor usando from beggining

```bash
./kafka-console-consumer.sh --bootstrap-server 127.0.0.1:9092 --topic mensagens --group consumidores --from-beginning
```

#### Reset do offset

```bash
./kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group consumidores --topic mensagens --reset-offsets --to-earliest --execute 
```

#### Novo consumidor para o grupo, as mensagens devem ser lidas desde o inicio

```bash
./kafka-console-consumer.sh --bootstrap-server 127.0.0.1:9092 --topic mensagens --group consumidores
```