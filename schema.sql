CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username varchar(255),
    password varchar(255)
);