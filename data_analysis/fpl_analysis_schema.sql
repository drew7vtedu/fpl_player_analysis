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
