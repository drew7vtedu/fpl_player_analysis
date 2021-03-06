DROP DATABASE IF EXISTS fplanalysis;
CREATE DATABASE IF NOT EXISTS fplanalysis;
USE fplanalysis;

CREATE TABLE players (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    games INT,
    starts INT,
    goals INT,
    assists INT,
    penalties_scored INT,
    xg FLOAT,
    npxg FLOAT,
    xa FLOAT,
    tackles_attempted INT,
    tackles_won INT,
    pressures INT,
    successful_pressures INT,
    dribbles_completed INT,
    dribbles_attempted INT,
    team_id INT
    -- points_last_season INT,
    -- current_points INT,
    -- price INT,
    -- ly_minutes INT,
);

CREATE TABLE teams (
    team_id INTEGER PRIMARY KEY,
    name TEXT,
    goals_for INT,
    goals_against INT,
    xg FLOAT,
    xga FLOAT
);

CREATE TABLE fixtures (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    home_team_id INT,
    home_goals INT,
    home_xg FLOAT,
    away_team_id INT,
    away_goals INT,
    away_xg FLOAT,
    gameweek INT,
    postponed BOOLEAN
);
