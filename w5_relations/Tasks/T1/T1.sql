-- Create artist table
CREATE TABLE  artist (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    followers INTEGER NOT NULL
);

-- Create album table
CREATE TABLE album (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    artist_id INTEGER NOT NULL,
    tracks INTEGER NOT NULL,
    FOREIGN KEY (artist_id) REFERENCES artist(id)-- makes this many to one relationship between album and artist this is many
);

INSERT INTO artist (name, followers) VALUES
('Garry B', 1240506),
('Daniel Ocean', 13405),
('Justin Perry', 4501),
('Kirk Button', 403);

INSERT INTO album (name, artist_id, tracks) VALUES
('Glass houses',1,12),
('Collar of bones',2,5),
('District zero',3,3),
('Cold shoulder',4,10),
('Dinner for one',1,14),
('Cat eat cat world',2,6),
('Brain teaser',3,4), 
('Bursting bubbles',4,11),
('Elephant in the room',4,11);

