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

    - INSERT INTO SELECT Statement

         It copies data from one table and inserts it into another table.

        - `
         INSERT INTO <table_name> (<field_1>, <field_2>, ...)
         SELECT <field_1>, <fiel_2>, ... FROM <table_target>;
         `



- SELECT

    Select columns from a table.

    - `
    select <columns> FROM <table or alias>;
    `

    - Select statements from different tables.

        - `
        SELECT <column_1>, <column_2>, ...
        FROM <table_1>, <table_2>, ...
        WHERE <condition>;
        `


- DELETE

    - `
    DELETE FROM <table_name> WHERE <field> = <value>;
    `

- UPDATE

    It's used to modify the existing records in a table.

    - `
    UPDATE <table_name>
    SET <column_1> = <value_1>, <column_2> = <value_2>, ...
    WHERE <condition>;
    `

- <details>
    <summary>
    JOINS
    </summary>

    ![joins_table](./images/joins-in-mysql.png)

    It's used to combine rows from two or more tables, based on a related column between them.

    - INNER JOIN

        ![inner_join](./images/innerjoin.gif)

        This keyword selects records that have matching values in both tables.

        `
        SELECT <column_name(s)>
        FROM <table_1>
        INNER JOIN <table_2>
        ON <table1.column_name> = <table2.column_name>;
        `

    - LEFT JOIN

        ![left_join](./images/leftjoin.gif)

        This keyword returns all records from the left table (table1), and the matching records from the right table (table2). The result is 0 records from the right side, if there is no match.


        `
        SELECT column_name(s)
        FROM table1
        LEFT JOIN table2
        ON table1.column_name = table2.column_name;
        `
    
    - RIGHT JOIN

        ![right_join](./images/rightjoin.gif)

        This keyword returns all records from the right table (table2), and the matching records from the left table (table1). The result is 0 records from the left side, if there is no match.

        `
        SELECT <column_name(s)>
        FROM <table_1>
        RIGHT JOIN <table_2>
        ON <table1.column_name> = <table2.column_name>;
        `

    - FULL JOIN

        ![full_join](./images/fulljoin.gif)

        This keyword returns all records when there is a match in left (table1) or right (table2) table records.

        `
        SELECT <column_name(s)>
        FROM <table_1>
        FULL OUTER JOIN <table_2>
        ON <table1.column_name> = <table2.column_name> WHERE <condition>;
        `

    - SELF JOIN.

        A self join is a regular join, but the table is joined with itself.

        `
        SELECT <column_name(s)>
        FROM <table_1> <T1>, <table_1> <T2>
        WHERE <condition>;
        `

    #

    - SELECT W/ JOIN

        `
        SELECT <comlumn_name(s)>
        FROM <table_name>
        <JOIN>
        `

    - UPDATE W/ JOIN

        `
        UPDATE <table_name>
        <JOIN> SET <update>
        WHERE <condition>
        `
    - DELETE W/ JOIN

        `
        DELETE <talbe_name>
        <JOIN> WHERE <condition>
        `

</details>

- <details>
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

    - LIKE

        It's used in a WHERE clause to search for a specified pattern in a column.

        `SELECT <column_1>, <column_2>, ...
        FROM <table_name>
        WHERE <column> LIKE <pattern>;
        `

        <details>
        <summary>
        Like Operators
        </summary>

        #

        -  The percent sign (%) represents zero, one, or multiple characters.

        - The underscore sign (_) represents one, single character.

        #

        |Like Operator|Description|
        |:---:|:---:|
        |`WHERE <column> LIKE 'a%'`|	Finds any values that start with "a"|
        |`WHERE <column> LIKE '%a'`|	Finds any values that end with "a"|
        |`WHERE <column> LIKE '%or%'`|	Finds any values that have "or" in any position|
        |`WHERE <column> LIKE '_r%'`|	Finds any values that have "r" in the second position|
        |`WHERE <column> LIKE 'a_%'`|	Finds any values that start with "a" and are at least 2 characters in length|
        |`WHERE <column> LIKE 'a__%'`|	Finds any values that start with "a" and are at least 3 characters in length|
        |`WHERE <column> LIKE 'a%o'`|Finds any values that start with "a" and ends with "o"|

        </details>

    - ORDER BY

        It's used to sort the result-set in ascending or descending order.

        `ex:`

        `
        SELECT <column_1>, <column_2>, ...
        FROM <table_name>
        ORDER BY <column_1>, <column_2>, ... ASC|DESC;
        `

    - LIMIT

        IT shows the limit specify of results.

        `ex:`

        `
        SELECT <column> FROM <table_name>
        LIMIT <value>;
        `

    - OFFSET

        It's like a pagination of limiit.

        `
        SELECT <column> FROM <table_name>
        LIMIT <value> OFFSET <value>;
        `

        The command OFFSET would be represented by:

        `SELECT <column> FROM <table_name>
        LIMIT <offset_value>, <limit_value>;
        `

</details>

- <details>
    <summary>
    FUNCTIONS
    </summary>

    - CONCAT

        It adds two or more expressions together.

        `
        CONCAT(<expression1>, <expression2>, <expression3>, ...)
        `

    - RAND

        Return a random decimal number (no seed value - so it returns a completely random number >= 0 and <1).

        `
        SELECT RAND();
        `

    - ROUND

        This function rounds a number to a specified number of decimal places.

        `
        ROUND(number, decimals)
        `

    - GROUP BY

        This statement groups rows that have the same values into summary rows, like "find the number of customers in each country".

        `
        SELECT column_name(s)
        FROM table_name
        WHERE condition
        GROUP BY column_name(s)
        ORDER BY column_name(s);
        `

    - MIN

        This function returns the smallest value of the selected column.

        `
        SELECT MIN(<column_name>)
        FROM <table_name>
        WHERE <condition>;
        `

    - MAX

        This function returns the largest value of the selected column.

        `
        SELECT MAX(<column_name>)
        FROM <table_name>
        WHERE <condition>;
        `

    - COUNT

        This function returns the number of rows that matches a specified criterion.

        `
        SELECT COUNT(<column_name>)
        FROM <table_name>
        WHERE <condition>;
        `

    - AVG

        This function returns the average value of a numeric column

        `
        SELECT AVG(<column_name>)
        FROM <table_name>
        WHERE <condition>;
        `

    - SUM

        This function returns the total sum of a numeric column. 

        `
        SELECT SUM(<column_name>)
        FROM <table_name>
        WHERE <condition>;
        `

</details>