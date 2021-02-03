import mysql.connector
from data_analysis import player_object
from data_analysis import team_object
from data_analysis import fantasy_value_metrics as metrics
from data_analysis.scraper import teams
from dotenv import load_dotenv
import os

class sql_db_connector(object):

    def __init__(self):
        load_dotenv()
        self.mydb = mysql.connector.connect(
          host="localhost",
          user=os.getenv("SQL_USER"),
          password=os.getenv("SQL_PASSWORD"),
          database="fplanalysis"
        )
        self.mycursor = self.mydb.cursor()


    '''
    using a test db to aviod making changes to production db
    '''
    def use_test_db(self):
        self.mycursor.execute("USE testfpl;")

    '''
    this will create a test db with an identical schema for testing purposes
    since this method will be called from the test directory the relative
    path to the schema file is different
    '''
    def create_test_db(self):
        schema = open("../data_analysis/test_schema.sql")
        sql = schema.read()
        schema.close()
        self.mycursor.execute(sql)

    '''
    run the sql schema to create the database on a mysql server
    '''
    def create_db(self):
        schema = open("./fpl_analysis_schema.sql")
        sql = schema.read()
        schema.close()
        self.mycursor.execute(sql)

    '''
    make sure we're using the correct database
    '''
    def use_db(self):
        self.mycursor.execute("USE fplanalysis;")

    def clear_all(self):
        self.mycursor.execute("CALL clear_all()")


    def insert_player(self, player):
        # sql = "INSERT INTO players (id, first_name, last_name, points_last_season, current_points, price, ly_minutes, minutes, xg, npxg, expected_assists, team_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        # values = (player.id, player.first_name, player.last_name, player.points_last_season, player.current_points, player.price, player.ly_minutes, player.minutes, player.xg, player.npxg, player.xa, player.team_id)
        sql = "INSERT INTO players (id, first_name, last_name, games, starts, goals, assists, penalties, xg, npxg, xa, tackles_attempted, tackles_won, pressures, successful_pressures, dribbles_completed, dribbles_attempted, team) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (player.id, player.first_name, player.last_name, player.games, player.starts, player.goals, player.assists, player.penalty_goals, player.xg, player.npxg, player.xa, player.tackles, player.tackles_won, player.pressures, player.pressure_regains, player.dribbles_completed, player.dribbles_attempted, player.team_id)
        self.mycursor.execute(sql, values)
        self.mydb.commit()

    def insert_team(self, team):
        sql = "INSERT INTO teams (team_id, goals_for, goals_against, xg, xga) VALUES (%s, %s, %s, %s, %s)"
        values = (team.id, team.goals_for, team.goals_against, team.xg, team.xga)
        self.mycursor.execute(sql, values)
        self.mydb.commit()

    def insert_fixture(self, fixture):
        sql = "INSERT INTO fixtures (home_team_id, home_goals, home_xg, away_team_id, away_goals, away_xg, gameweek, postponed) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (fixture.get_home(), fixture.get_home_goals(), fixture.get_hxg(), fixture.get_away(), fixture.get_away_goals(), fixture.get_axg(), fixture.get_gameweek(), fixture.get_postponed())
        self.mycursor.execute(sql, values)
        self.mydb.commit()

    def set_names(self):
        for team in teams:
            sql = "UPDATE teams SET name = %s WHERE team_id = %s"
            values = (team, teams.index(team) + 1)
            self.mycursor.execute(sql, values)
            self.mydb.commit()


    def get_top_scorer(self):
        sql = "SELECT first_name, last_name, current_points FROM players ORDER BY current_points LIMIT 1"
        self.mycursor.execute(sql)
        myresult = self.mycursor.fetchall()
        for x in myresult:
            print(x)

    def get_strength_of_schedule(self):
        sql = '''
        SELECT c.name, SUM(b.xg - b.xga) AS opp_goal_diff
        FROM (SELECT team_id, away_team_id AS opp_id
        FROM teams JOIN fixtures ON team_id = home_team_id
        WHERE home_xg IS NOT NUll
        UNION
        SELECT team_id, home_team_id AS opp_id
        FROM teams JOIN fixtures ON team_id = away_team_id
        WHERE home_xg IS NOT NULL) a
        JOIN teams b ON a.opp_id = b.team_id
        JOIN teams c ON c.team_id = a.team_id
        GROUP BY a.team_id ORDER BY opp_goal_diff DESC;
        '''
        self.mycursor.execute(sql)
        myresult = self.mycursor.fetchall()
        for x in myresult:
            print(x)


if __name__ == "__main__":
    db = sql_db_connector()
    # db.create_db()
    # db.set_names()
    db.get_strength_of_schedule()
