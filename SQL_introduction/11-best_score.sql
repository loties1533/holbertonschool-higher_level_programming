-- scipt qui affiche le score et name , trié par la meilleur score (uniquement >= 10)
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
