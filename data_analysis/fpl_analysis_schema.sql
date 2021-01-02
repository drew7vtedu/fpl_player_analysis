DROP DATABASE IF EXISTS fplanalysis;
CREATE DATABASE IF NOT EXISTS fplanalysis;
USE fplanalysis;

CREATE TABLE players (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    points_last_season INT,
    current_points INT,
    price INT,
    ly_minutes INT,
    minutes INT,
    xg FLOAT,
	  expected_assists FLOAT,
    team_id INT
    );

CREATE TABLE teams (
    team_id INTEGER PRIMARY KEY,
    goals_for INT,
    goals_against INT,
    xg FLOAT,
    xga FLOAT,
    schedule_id INT
);

CREATE TABLE fixtures (
    id INT AUTO_INCREMENT
    team_id INT,
    gameweek INT,
    opponent TEXT
);
