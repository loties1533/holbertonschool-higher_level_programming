-- script qui liste les serie du genre comedy
-- utilise JOIN pour relier les tables et WHERE pour filtrer par genre 'comedy'
SELECT tvs.title 
FROM tv_shows AS tvs
JOIN tv_show_genres AS tvsg ON tvs.id = tvsg.show_id
JOIN tv_genres AS tvg ON tvsg.genre_id = tvg.id
WHERE tvg.name = 'Comedy'
ORDER BY tvs.title ASC;
