SHOW DATABASES;
CREATE OR REPLACE DATABASE viagens;
USE viagens;
CREATE OR REPLACE TABLE users(
    id INT, name VARCHAR(255) NOT NULL, email VARCHAR(100) UNIQUE,
    address VARCHAR(50) NOT NULL, birth DATE NOT NULL
    );
CREATE OR REPLACE TABLE destination(
    id INT,name VARCHAR(255) NOT NULL, description TEXT NOT NULL);

CREATE OR REPLACE TABLE booking(
    id INT, id_user INT, id_destination INT, date DATE, status VARCHAR(255)
);
