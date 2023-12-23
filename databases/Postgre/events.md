# 🎉 Events

# [🔫 Triggers](https://www.postgresql.org/docs/current/plpgsql-trigger.html)

Triggers, são as operações realizadas de forma espontânea para eventos específicos. Quando tratamos dos eventos, estes podem ser tanto um `INSERT` quanto um `UPDATE`, ou mesmo um `DELETE`. Assim, podemos definir determinadas operações que serão realizadas sempre que o evento ocorrer.

- Lembrado que para todo trigger precisamos de uma `função` que será chamada toda vez que o evento for disparado.

- `OLD` se refere ao estado antigo da linha(`ROW`) e `NEW` ao estado novo.

## Trigger Function

- Toda função trigger tem que retornar um tipo `trigger` e não pode ter parametros.

```SQL
CREATE OR REPLACE FUNCTION trigger_function_name
RETURNS trigger AS $
BEGIN
<logic>
RETURN NEW;
END;
$;
```

## [Create Trigger](https://www.postgresql.org/docs/current/sql-createtrigger.html)

```SQL
CREATE OR REPLACE TRIGGER <trigger_name> <when> <event> ON
<table_name>  <FOR [ EACH ] { ROW | STATEMENT }> or <WHEN ( condition )>
EXECUTE FUNCTION <trigger_function>;
```

`<when>` - Quando a ação deve ser tomada.

|`BEFORE`|Antes do evento|
|:---:|:---:|
|`AFTER`|Despois do evento|
|`INSTEAD`|Ao invés do evento.|

`event` - eventos; `INSERT`, `UPDATE`, `DELETE` e `TRUNCATE`.


## [Transactions](https://www.postgresql.org/docs/current/tutorial-transactions.html)

## [Erros](https://www.postgresql.org/docs/15/plpgsql-control-structures.html#PLPGSQL-ERROR-TRAPPING)

### [Tabela de erros](https://www.postgresql.org/docs/current/errcodes-appendix.html)

## [Cursores](https://www.postgresql.org/docs/15/plpgsql-cursors.html)