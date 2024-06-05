DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    passwd TEXT NOT NULL,
    role TEXT NOT NULL
);

INSERT INTO users (username, email, passwd, role) VALUES ("yvan", "yvan@gmail.com", "passwd", "ADMIN")