-- list all comedy shows
SELECT tv_shows.title
FROM tv_genres
     INNER JOIN tv_show_genres
     INNER JOIN tv_shows
     	   ON tv_genres.id=tv_show_genres.genre_id
	   AND tv_show_genres.show_id=tv_shows.id
WHERE tv_genres.name='Comedy'
ORDER BY tv_shows.title ASC;
