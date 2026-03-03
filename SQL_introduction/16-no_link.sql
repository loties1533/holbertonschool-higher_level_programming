-- script qui liste tous les enregistrement  de second_table et filtre les nom vide ou NULL
-- affiche score puis name , triés par score décroissant
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
