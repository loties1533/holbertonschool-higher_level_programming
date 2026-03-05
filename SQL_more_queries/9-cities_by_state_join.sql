-- script qui liste toute les villes et etats correspondant
-- utilise JOIN pour faire correspondre/associeer les tables 'cities' et 'states'
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;