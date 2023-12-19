-- Script that prepares a MySQL server for the project

-- Creates database if it doesn't exists
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
USE hbnb_test_db;

-- Creates a new user if it doesn't exist, with password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grants all privileges on the database hbnb_test_db to hbnb_test
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grants SELECT privilege on the database performance_schema to hbnb_test
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
