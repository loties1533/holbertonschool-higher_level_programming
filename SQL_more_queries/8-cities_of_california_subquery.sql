-- Script pour lister les villes de Californie (Subquery/sous requête)
-- Filtre la table 'cities' selon l'ID trouvé et trie par ID croissant
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;