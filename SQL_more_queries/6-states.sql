-- script qui crée la base de données hbtn_0d_usa et la table states
-- table states avec ID auto-incrémenté et clé primaire, et name qui ne peut pas etre nul
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
