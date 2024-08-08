-- A  SQL script that creates a table users with unique email and name
-- If the table already exists, your script should not fail

CREATE TABLE  IF NOT EXISTS  users (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255)
);
