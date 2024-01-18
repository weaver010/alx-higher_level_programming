-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT g.name AS name
FROM tv_shows e INNER JOIN tv_show_genres es
ON e.id = es.show_id
INNER JOIN tv_genres AS b
ON es.genre_id = b.id
WHERE e.title = 'Dexter'
ORDER BY b.name;

