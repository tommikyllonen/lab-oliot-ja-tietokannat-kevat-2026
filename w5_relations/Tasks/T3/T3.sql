SELECT artist.name AS name, sum(album.tracks) AS total_tracks FROM artist
JOIN album ON artist.id = album.artist_id
GROUP BY artist.name --This makes artist appear only once in the result and sums up the tracks of all albums of that artist
ORDER BY artist.name ASC;


--           +--------------+--------------+
--           |     name     | total_tracks |
--           +--------------+--------------+
--           | Daniel Ocean | 11           |
--           | Garry B      | 26           |
--           | Justin Perry | 7            |
--           | Kirk Button  | 32           |
--           +--------------+--------------+

