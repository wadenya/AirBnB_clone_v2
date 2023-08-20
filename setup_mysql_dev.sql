-- prepares a MySQL server for the project

-- create db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- crestes user and grant privileges
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';
ALTER USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO hbnb_dev@localhost;
GRANT SELECT ON performance_schema.* TO hbnb_dev@localhost;
FLUSH PRIVILEGES;