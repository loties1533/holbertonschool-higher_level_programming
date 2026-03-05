-- script qui liste tout les genres de la serie dexter
-- JOIN pour relier les tables et WHERE pour filtrer par titre
SELECT tvg.name
FROM tv_genres AS tvg
JOIN tv_show_genres AS tvsg ON tvg.id = tvsg.genre_id
JOIN tv_shows AS tvs ON tvsg.show_id = tvs.id
WHERE tvs.title = 'Dexter'
ORDER BY tvg.name ASC;
