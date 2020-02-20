-- SQLite
CREATE TABLE användare (
    användarnamn VARCHAR(32) UNIQUE,
    lösenord VARCHAR(255),
    id INTEGER PRIMARY KEY AUTOINCREMENT  NOTNULL)

    -- INSERT INTO användare (användarnamn, lösenord)
    --     VALUES
    --         ('Linus', 'bla'),
    --         ('bi', 'ba');