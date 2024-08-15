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