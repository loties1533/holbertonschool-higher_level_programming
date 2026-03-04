-- script pour créé une table 'force_name' (bdd passer en argument)
-- le script crée une table ou le nom ne peut pas etre nul (vide)
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
