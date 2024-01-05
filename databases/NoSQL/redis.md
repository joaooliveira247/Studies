# <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/redis/redis-original.svg" width="25px"> Redis

|Re|di|s|
|:---:|:---:|:---:|
|REmote|DIctionary|Server|

- Banco de dados Chave-valor em memória.

- Rápido

- Suporte a varios tipos de dados

- Pode usar disco para persistência

- Cache de Sessões

- Cache de Páginas

- Não existe padrão

- Suporte a Partição (divisão de dados entre instâncias)

- Suporte a Data Streaming

- Suporte a Cluster

## `SELECT`

- `SELECT <int>`

Troca o banco de dados, o padrão é zero.

## `EXISTS`

- `EXISTS <key>`

Verifica se uma chave existe

## `TYPE`

- `TYPE <key>`

Verifica o tipo de um valor.

## `EXPIRE`

- `EXPIRE <key> <time>`

Define o tempo de expiração de uma chave, por padrão o tempo é definido em segundo, para milisegundo use `PEXPIRE`

## `PERSIST`

- `PERSIST <key>`

remove o tempo de expiração de uma chave

## `TTL`

- `TTL <key>`

verifica o tempo de expiração de uma chave, caso `-1` um tempo não foi definito, para verificar em milisegundos user `PTTL`

## Tipos de dados

- Strings

- Hashes

- Lists

- Sets

### `String`

- `SET <key> <value>` | `SET <key> <value> EX <time> NX`

Define um valor

|Argumentos|Funções|
|:---:|:---:|
|`<EX>`|Define uma expiração em Segundos|
|`<PX>`|Define uma expiração em Milisegundos|
|`<NX>`|Só funciona se a cave **não** existir|
|`<XX>`|Só funciona se a chave já existir|

`ex:`

```shell
SET 1 "Abacate"
```

```shell
SET 1 "Abacate" EX 50 NX
```

- `GET <key>`

Pega um valor


`ex:`

```shell
GET 1
```

- `DEL <key>`

Deleta uma chave

`ex:`

```shell
DEL 1
```

- `MSET <key> <value> <key> <value> ...`

Define varios valores de uma vez.

`ex:`

```shell
MSET 101 "Abacate" 102 "Maça" 103 "Laranja"
```

- `GETRANGE <key> <start> <end>`

Retorna a slice do valor.

`ex:`

```shell
GETRANGE 1 0 3
>>> Abac
```

- `GETSET <key> <value>`

Atualiza o valor.

`ex:`

```shell
GETSET 1 "Laranja"
```

- `MGET <key> <key> ...`

Retorna o valor de varias keys

`ex:`

```shell
MGET 1 2 3
>>> 1) "Laranja"
>>> 2) "Banana"
>>> 3) "Abacate"
```

- `STRLEN <key>`

Retorna o tamanho do valor

`ex:`

```shell
STRLEN 1
>>> (integer) 1
```

### `Hashes`

Conjunto de campos/valores, associados a uma chave

- `HMSET <key> <field> <value> <field> <value> ...`

Define valores.

`ex:`

```shell
HMSET CADASTRO Nome Luiz Profissao Engenheiro Cidade "Rio de Janeiro"
```

- `HDEL <key> <field>`

Deleta um campo, para deletar basta usar o `DEL <key>`

- `HGETALL <key>`

Retorna todas as chaves e valores

- `HMGET <key> <field> ...`

Retorna somente os campos especificados

- `HVALS <key>`

Retorna todos os calores

- `HKEYS <key>`

Retorna todos os fields.

- `HEXISTS <key> <field>`

Verifica se o campo existe.

- `HLEN <key>`

Verifica o numero de fields

### `Lists`

Lista de strings com chave unica que podem ser inseridas separadamente

- `LPUSH <key> <value> <value> ...`

Inseri valores a esquerda 

`ex:`

```shell
LPUSH databases MongoDB PostgreSQL
```

- `RPUSH <key> value`

Inseri valores a direita

`ex:`

```shell
RPUSH databases DynamoDB
```

- `LRANGE <key> <start> <end>`

Retorna o slice da list

- `LINSERT <key> <arg> <pos> <value>`

|Arg|Função|
|:---:|:---:|
|BEFORE|Antes de|
|After|Depois de|

\<pos>: item da lista

`ex:`

```Shell
LINSERT databases BEFORE DynamoDB MySQL
```

- `LSET <key> <index> <value>`

Atualiza valor me dado indice

- `LINDEX <key> <index>`

Retorna valor em dado index

- `LLEN <key>`

Retorna o tamanho da lista

- `RPOP <key>`

Remove um valor a direita

- `LPOP <key>`

Remove um valor a esquerda

### `Sets`

Coleção não ordenada, não aceita valores repetidos.

- `SADD <key> <value> <value> ...`

Inseri valores, se o valor já existir retornará 0

- `SMEMBERS <key>`

Recupera valores.

- `SCARD <key>`

Retorna o número de membros(valores)

- `SISMEMBER <key> <value>`

Verifica se o \<value> faz parte do set

- `SREM <key> <value> ...`

Remove 1 ou n valores

- Operações sobre sets

|Função|Descrição|
|:---:|:---:|
|`SDIFF <key> <key>`|Mostra a diferença entre dois sets|
|`SINTER <key> <key>`|Mostra a interjeição entre dois sets|

### `Sets Ordenados`

Valores não repetidos, ordenados baseados em score

- `ZADD <key> <score> <value>`

Inseri um valor com um score

- `ZCARD <key>`

Retorna o número de elementos

- `ZRANK <key> <value>`

Retorna o indice de um valor

- `ZCOUNT <key> <start> <end>`

Conta o número de valores em determinado intervalo dos scores

- `ZSCORE <key> <value>`

Retorna o score de um membro

- `ZRANGE <key> <start> <end>`

Retorna os membros em dado intervalo,
se passada a flag `WITHSCORES` no final retorna os scores junto.

- `ZREM <key> <value>`

Remove um valor
