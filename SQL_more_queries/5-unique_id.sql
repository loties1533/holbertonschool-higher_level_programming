-- script pour créé une table unique_id avec une valeur par defaut pour l ID(INT) qui est unique 
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
