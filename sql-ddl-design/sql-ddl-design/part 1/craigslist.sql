CREATE TABLE regions(
    id SERIAL PRIMARY KEY,
    region_name VARCHAR NOT NULL
);

CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    username VARCHAR NOT NULL,
    user_password VARCHAR NOT NULL,
    preferred_region VARCHAR
);

CREATE TABLE categories(
    id SERIAL PRIMARY KEY,
    category_name VARCHAR NOT NULL
);

CREATE TABLE posts(
     id SERIAL PRIMARY KEY,
     title TEXT NOT NULL,
     post_text TEXT,
     post_location VARCHAR NOT NULL,
     user_id INT REFERENCES users(id),
     region_id INT REFERENCES regions(id),
     category_id INT REFERENCES categories(id)
);