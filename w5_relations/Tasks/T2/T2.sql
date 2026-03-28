SELECT artist.name AS artist, artist.followers, album.name AS album, album.tracks AS tracks FROM artist
JOIN album ON artist.id = album.artist_id 
ORDER BY artist.name ASC, album.name ASC;