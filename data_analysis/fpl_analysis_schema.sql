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
	  npxg FLOAT,
	  expected_assists FLOAT,
    team_id INT
    );

CREATE TABLE teams (
    team_id INTEGER PRIMARY KEY,
    goals_for INT,
    goals_against INT,
    xg FLOAT,
    npxg FLOAT,
    xga FLOAT,
    schedule_id INT
);

CREATE TABLE schedules (
    team_id INT PRIMARY KEY,
    gameweek INT,
    opponent TEXT
);
