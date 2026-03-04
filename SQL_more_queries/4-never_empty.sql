-- script qui crée la id_not_null de table sur serveur MySQL
-- l id de la table ne peut pas etre nul (par defaut 1)
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
)
