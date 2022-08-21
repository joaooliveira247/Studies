# Data Definition Language

it's a syntax for creating and modifying database objects such as tables, indices, and users. DDL statements are similar to a computer programming language for defining data structures, especially database schemas.

- CREATE

    - `CREATE DATABASE <db_name>;`

        Create a database.

    - `
    CREATE TABLE <table_name> (
        id INT AUTO_INCREMENT,
        title VARCHAR(255) NOT NULL,
        payment DATE,
        alor DOUBLE,
        PRIMARY KEY (id)
    );
    `

        Create a table in your database.

    - `
    CREATE INDEX index_name ON table_name (column1, column2, ...);
    `

        Creates an index on a table. Duplicate values are allowed.

- ALTER

    - `
    ALTER TABLE <table_name> DROP COLUMN <column>; 
    `

        This command is making an alter in the table dropping(deleting) a column.
    
    - `
    ALTER TABLE <table_name> ADD COLUMN <column>;
    `

        This command is creating a new column at the table

- DROP

    - `
    DROP DATABASE <db_name>;
    `

        Delete a database.

    - `
    DROP TABLE <table_name>;
    `

        Delete a table.

- <details>
    <summary>
    CONSTRAINS
    </summary>

    SQL constraints are used to specify rules for the data in a table.

    They are used to limit the type of data that can go into a table. This ensures the accuracy and reliability of the data in the table. If there is any violation between the constraint and the data action, the action is aborted.


    `CREATE TABLE <table_name> (
    <column_1> <datatype> <constraint>,
    <column_2> <datatype> <constraint>,
    <column_3> <datatype> <constraint>,
    ....
    );`

    - NOT NULL

        Ensures that a column can't have a NULL value.

    - UNIQUE 

        Ensures that all values in a column are different

    - PRIMARY_KEY 

        A combination of NOT NULL and UNIQUE. Uniquely identifies each row in a table. 

    - FOREIGN_KEY

        Prevents action that would destroy links between tables.

    - CHECK 

        Ensures that the values in a column satisfies a specific condition.

    - DEFAULT 

        Sets a default value for a column if no value is specified.

    - CREATE_INDEX 

        Used to create and retrieve data from database very quickly.


</details>