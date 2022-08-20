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