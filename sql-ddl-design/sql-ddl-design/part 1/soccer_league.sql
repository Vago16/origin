CREATE TABLE teams(
    id SERIAL PRIMARY KEY,
    team_name VARCHAR NOT NULL,
    area VARCHAR NOT NULL
);

CREATE TABLE referees(
     id SERIAL PRIMARY KEY,
     referee_name VARCHAR NOT NULL
);

CREATE TABLE players(
     id SERIAL PRIMARY KEY,
     player_name VARCHAR NOT NULL,
     personal_info TEXT,
     team_id INT REFERENCES teams(id)
);

CREATE TABLE matches(
     id SERIAL PRIMARY KEY,
     match_date DATE NOT NULL,
     start_time TIMESTAMP NOT NULL,
     match_location VARCHAR NOT NULL,
     home_team_id INT REFERENCES teams(id),
     away_team_id INT REFERENCES teams(id),
     referee_id INT REFERENCES referees(id)
);

CREATE TABLE season(
     id SERIAL PRIMARY KEY,
     team_id INT REFERENCES teams(id),
     player_id INT REFERENCES players(id),
     match_id INT REFERENCES matches(id)
);

CREATE TABLE rankings(
     id SERIAL PRIMARY KEY,
     team_id INT REFERENCES teams(id),
     player_id INT REFERENCES players(id),
     match_id INT REFERENCES matches(id)
);