# Data Manipulation Language

it's a computer programming language used for adding (inserting), deleting, and modifying (updating) data in a database. A DML is often a sublanguage of a broader database language such as SQL, with the DML comprising some of the operators in the language.

- <details>
    <summary>
    Order of Execution
    </summary>

    1. `FROM`
    2. `WHERE`
    3. `GROUP BY`
    4. `HAVING`
    5. `SELECT`
    6. `ORDER BY`
    7. `LIMIT`

</details>

- INTERACT

    - `
    SHOW databases;
    `

        Show all databases.

    - `
    USE <db_name>;
    `

        Select a database.

    - `
    SHOW tables;
    `

        Show all tables.

    - `
    describe <table_name>;
    `

        show the description of a table

- INSERT

    Insert values into a table.

    - `
    INSERT INTO <table> (<field>) values (<value>);
    `

    - `
    INSERT INTO <table> (<field_1>, <field_2>. ...) VALUES
    (<value_1>, <value_2>, ...);
    `

- SELECT

    - `
    select <columns> FROM <table or alias>;
    `

        select columns from a table

- DELETE

    - `
    DELETE FROM <table_name> WHERE <field> = <value>;
    `

- UPDATE

    - 

- <details open>
    <summary>
    CLAUSES
    </summary>

    - AS

        Rename column or table with alias.

        `ex:`

        `SELECT <field> AS <alias>, <field> AS <alias>
        FROM <table>;
        `

    - WHERE

        Filter query to match a condition.

        `ex:`

        `
        SELECT <field> FROM <table> WHERE <condition>;
        `

    - AND

        It's used with WHERE to only include rows where both conditions are true.

        `ex:`

        `
        SELECT <field> FROM <table>
        WHERE <condition> AND <condition>;
        `

    - BETWEEN

        It's used to select values within a given range. The values can be numbers, text, or dates.

        `ex:`

        `
        SELECT <fields> FROM <table>
        WHERE <condition>
        BETWEEN <start> AND <stop>;
        `

    - IN

        Specify multiple values, when use WHERE.

        `ex:`

        `SELECT first_name, last_name, email 
        FROM users
        WHERE id in (10, 100, 90);
        `

</details>