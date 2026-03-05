-- script qui liste les serie avec au moins une categorie/genre
-- affiche le titre et l'ID de la categorie/genre triés par titre et genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
