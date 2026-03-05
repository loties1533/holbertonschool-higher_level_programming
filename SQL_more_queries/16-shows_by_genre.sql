-- script pour lister toutes les serie par 'genre' associé
-- avec LEFT JOIN pour toutes les serie sans 'genre' (NULL)
SELECT tvs.title, tvg.name
FROM tv_shows AS tvs
LEFT JOIN tv_show_genres AS tvsg ON tvs.id = tvsg.show_id
LEFT JOIN tv_genres AS tvg ON tvsg.genre_id = tvg.id
ORDER BY tvs.title ASC, tvg.name ASC; 
