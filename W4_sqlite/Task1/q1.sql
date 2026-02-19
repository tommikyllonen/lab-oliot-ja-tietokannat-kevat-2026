.mode table
.headers ON

CREATE TABLE device (
  id    INTEGER PRIMARY KEY AUTOINCREMENT,
  mac   TEXT UNIQUE NOT NULL,
  os    TEXT NOT NULL,
  model TEXT NOT NULL
);