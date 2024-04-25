UPDATE
    users
SET 
    name = "new name", email = "newemail@test.com" 
WHERE 
    id = 1;

SELECT
    *
FROM
    users;

DELETE FROM 
    users
WHERE
    id = 2;