DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    passwd TEXT NOT NULL,
    role TEXT NOT NULL,
    UNIQUE(id, username, email)
);

INSERT INTO users (username, email, passwd, role) VALUES ("yvan", "yvan@gmail.com", "passwd", "ADMIN")