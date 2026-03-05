-- script qui liste les séries avec leur genre (même sans genre)
-- affiche titre et l'ID de la catégorie/genre triés par titre et genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
