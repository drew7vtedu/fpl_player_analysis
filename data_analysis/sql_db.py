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


    def use_test_db(self):
        self.mycursor.execute("USE testfpl;")

    def create_test_db(self):
        schema = open("./test_schema.sql")
        sql = schema.read()
        self.mycursor.execute(sql)

    def create_db(self):
        schema = open("./fpl_analysis_schema.sql")
        sql = schema.read()
        self.mycursor.execute(sql)



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
        values = (fixture.home_team_id, fixture.away_team_id, fixture.gameweek)
        self.mycursor.execute(sql, values)
        self.mydb.commit()


    def get_top_scorer(self):
        sql = "SELECT first_name, last_name, current_points FROM players ORDER BY current_points LIMIT 1"
        self.mycursor.execute(sql)
        myresult = self.mycursor.fetchall()
        for x in myresult:
            print(x)

if __name__ == "__main__":
    db = sql_db_connector()
    player = player_object.player_obj(1, "first", "last", 0, 0, 1, 0, 1, 1)
    #db.clear_all()
    db.create_db()
    db.use_db()
    db.insert_player(player)
    #db.get_top_scorer()
