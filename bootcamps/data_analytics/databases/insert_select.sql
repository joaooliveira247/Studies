INSERT INTO 
    users(id, name, email, birth, address)
VALUES
    (1, "some name", "test@test.com", "1999-03-02", "somewhere");

INSERT INTO
    destination(id , name, description)
VALUES 
    (1, "somewhere", "something");

INSERT INTO 
    booking (id, id_user, id_destination, status, `date`) 
VALUES
    (1, 1, 1, "pending", "2023-11-11");

SELECT
    * 
FROM
    users;

SELECT
    *
FROM
    users
WHERE
    (address = "somewhere");