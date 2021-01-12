import mysql.connector
from data_analysis import player_object
from data_analysis import team_object
from data_analysis import fantasy_value_metrics as metrics
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
        sql = "INSERT INTO players (id, first_name, last_name, points_last_season, current_points, price, ly_minutes, minutes, xg, npxg, expected_assists, team_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (player.id, player.first_name, player.last_name, player.points_last_season, player.current_points, player.price, player.ly_minutes, player.minutes, player.xg, player.npxg, player.xa, player.team_id)
        self.mycursor.execute(sql, values)
        self.mydb.commit()

    def insert_team(self, team):
        sql = "INSERT INTO teams (id, name, goals_for, goals_against, xg, npxg, xga) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (team.id, team.map_team(team.id), team.goals_for, team.goals_against, team.xg, team.npxg, team.xga)
        self.mycursor.execute(sql, values)
        self.mydb.commit()

    def insert_fixture(self, fixture):
        sql = "INSERT INTO fixtures (home_team_id, away_team_id, gameweek) VALUES (%s %s %s)"
        values = (fixture.home, fixture.away, fixture.gameweek)
        self.mycursor.execute(sql, values)
        self.mydb.commit()


    def get_top_scorer(self):
        sql = "SELECT first_name, last_name, current_points FROM players ORDER BY current_points LIMIT 1"
        self.mycursor.execute(sql)
        myresult = self.mycursor.fetchall()
        for x in myresult:
            print(x)
