-- script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT s.title AS title, g.genre_id AS genre_id
 FROM tv_shows AS b 
	INNER JOIN tv_show_genres AS e
	ON b.id = e.show_id
 ORDER BY b.title, e.genre_id;
