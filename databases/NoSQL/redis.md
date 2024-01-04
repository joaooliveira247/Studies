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