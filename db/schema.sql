DROP TABLE IF EXISTS urls;

CREATE TABLE urls ( 
    id PRIMARY KEY,
    short_url TEXT NOT NULL,
    long_url TEXT NOT NULL
);