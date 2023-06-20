-- from the terminal run:
-- psql < outer_space.sql

DROP DATABASE IF EXISTS outer_space;

CREATE DATABASE outer_space;

\c outer_space

CREATE TABLE galaxies (
  id SERIAL PRIMARY KEY,
  galaxy_name TEXT NOT NULL,
  size FLOAT
);

CREATE TABLE stars (
  id SERIAL PRIMARY KEY,
  star_name TEXT NOT NULL,
  size FLOAT,
  galaxy_id INT REFERENCES galaxies(id)
);

CREATe TABLE moons (
  id SERIAL PRIMARY KEY,
  moon_name TEXT NOT NULL,
  size FLOAT
);

CREATE TABLE planets
(
  id SERIAL PRIMARY KEY,
  planet_name TEXT NOT NULL,
  orbital_period_in_years FLOAT NOT NULL,
  galaxy_id INT REFERENCES galaxies(id),
  star_id INT REFERENCES stars(id),
  moon_id INT REFERENCES moons(id)
);
