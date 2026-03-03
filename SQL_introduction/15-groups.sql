-- script qui liste le nombre de personne (number) par score dans la table second_table
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;