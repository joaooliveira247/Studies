# <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg" width="15px"> MongoDB

- Open source

- Multiplataforma

- Escalável

- Orientado a documentos: (BSON/JSON)

- Permite documentos aninhados

- Indexados: pode=se buscar o conteúdo dos documentos

- Não tem schema fixo

- Não tem integridade referencial

## Tipos de dados:

- String

- Integer

  - Default is Int32

  - Long is used to express Int64

- Boolean

- Double

- Array

- Timestamp

- Date

- Object

  - Pode ser um JSON/BSON

## Glosário:

|      SQL       |     Mongo      |
| :------------: | :------------: |
| Banco de dados | banco de dados |
|     Tabela     |    Coleção     |
|     Linha      |   Documento    |
|     Coluna     |     Campo      |

## 🖥️ Comandos

### `Use`

- Acessa o documento, caso o mesmo não exista ele cria.

`ex:`

```shell
use mydb;
```

⚠️ observação:

- O banco só será persistido se algum dado for inserido.

---

### `show`

- Mostra informações sobre o banco ou collections

`ex:`

```shell
show dbs;
```

- Mostra todos os bancos de dados.

```shell
show collections;
```

- Mostra collections presentes em um banco de dados.

---

### `createCollection`

cria uma coleção explicitamente.

```shell
db.createCollection("myCollection");
```

---

### `Insert`

insere valores em bum banco.

- `insertOne()`

Insere um unico documento no banco.

`ex:`

```shell
db.collection.insertOne({key: value, ...});
```

- `insert()`

Insere um ou mais valores no banco.

```shell
db.collection.insert([{key: value, ...}, {key: value, ...}, ...]);
```

---

### `find`

recupera valores de um banco.

- `findOne()`

Recupera um único valor.

```shell
db.collection.findOne();
```

- `find()`

Recupera todos os valores

```shell
db.collection.find();
```

- Encontrando valores especificos:

```
db.collection.find({field: value, ...});
```

- Operadores:

| Operador |       Função       |
| :------: | :----------------: |
|   $eq    |       Igual        |
|   $gt    |     Maior que      |
|   $gte   |   Maior ou igual   |
|   $lt    |     Menor que      |
|   $lte   | Menor ou igual que |
|   $ne    |    Diferente de    |
|   $in    |       Contém       |
|   $nin   |     Não contém     |

[Mongo Operator Documentation](https://www.mongodb.com/docs/manual/reference/operator/query/)

### ``

```shell
db.collection.find({field: {Operator: value}});
```

---

### `Update`

Atualiza valores.

```shell
db.collection.update({where}, {$set: value});
```

`ex:`

```shell
db.collection.update({name: "name_1"}, {$set: {age: 18}});
```

### [`Save`](https://www.mongodb.com/docs/v3.6/reference/method/db.collection.save/)

se o documento existir atualiza

```shell
db.collection.save(<Document>, );
```

`ex:`

```shell
db.products.save(
    { item: "envelopes", qty : 100, type: "Clasp" },
    { writeConcern: { w: "majority", wtimeout: 5000 } }
)
```

### `Delete`

- `deleteOne()`

Exclui um único documento, mesmo que o criterio retorne vários

```shell
db.collection.deleteOne();
```

`ex:`

```shell
try {
   db.orders.deleteOne( { "_id" : ObjectId("563237a41a4d68582c2509da") } );
} catch (e) {
   print(e);
}
```

- `deleteMany()`

Exclui todos os documentos conforme o critério

```shell
db.collection.deleteMany();
```

`ex:`

```
try {
   db.orders.deleteMany( { "client" : "Crude Traders Inc." } );
} catch (e) {
   print (e);
}
```

- `remove()`

Exclui todos os documentos da coleção

```shell
db.collection.remove();
```

- `remove()`

Exclui todos os documentos da coleção

### `Drop`

Exclui uma coleção

```shell
db.collection.drop();
```

### `Extras:`

|     Comando     |            Descrição            |
| :-------------: | :-----------------------------: |
| cursor.limit(n) |  limita em n o número da query  |
| cursor.prety()  | mostra a query de outra maneira |

[Mongo Documentation](https://www.mongodb.com/docs/manual/reference/method/js-cursor/)
