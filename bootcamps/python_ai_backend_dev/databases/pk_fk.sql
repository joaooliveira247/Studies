ALTER TABLE
    users
MODIFY COLUMN 
    id INT AUTO_INCREMENT, 
ADD 
    PRIMARY KEY(id);

ALTER TABLE 
    booking 
ADD CONSTRAINT 
    fk_booking_users 
FOREIGN KEY(id_user) 
REFERENCES 
    users (id);