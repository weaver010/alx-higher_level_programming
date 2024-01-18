-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT g.name AS genre, COUNT(gs.genre_id) AS number_of_shows
FROM tv_shows r INNER JOIN tv_show_genres es
ON r.id = es.show_id
INNER JOIN tv_genres e
ON es.genre_id = e.id
GROUP BY e.name
ORDER BY number_of_shows desc;
