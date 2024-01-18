-- a script that lists all shows contained in the database hbtn_0d_tvshows.
SELECT s.title AS title, g.genre_id AS genre_id
FROM tv_shows AS r LEFT JOIN tv_show_genres t
	ON r.id = t.show_id
ORDER BY r.title, t.genre_id;
