DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    passwd TEXT NOT NULL,
    role TEXT NOT NULL,
    UNIQUE(id, username, email)
);

INSERT INTO users (username, email, passwd, role) VALUES ("admin", "admin@gmail.com", "$2a$12$3/oG4v.IVeUC89oRJqKjzOSrzlQHh4j8tb3prnAO66Us/N6skzD.m", "ADMIN")