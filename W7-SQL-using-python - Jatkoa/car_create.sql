-- Purpose: Create the car table.
-- usually "IF NOT EXISTS" is used to avoid errors when the table already exists.
-- The "FOREIGN KEY" constraint is used to enforce referential integrity.
-- The "REFERENCES" keyword is used to specify the parent table and column.
CREATE TABLE IF NOT EXISTS car (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    brand TEXT NOT NULL,
    model TEXT NOT NULL,
    year INTEGER NOT NULL,
    color TEXT NOT NULL,
    engine_id INTEGER NOT NULL,
    owner_id INTEGER,
    FOREIGN KEY (engine_id) REFERENCES engine(id)
);
