-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create user if it doesn't exist and set its password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on hbnb_test_db to hbnb_test
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Flush the privileges to ensure they take effect
FLUSH PRIVILEGES;
