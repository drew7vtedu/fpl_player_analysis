import mysql.connector
import player_object
import team_object
import fantasy_value_metrics as metrics

class sql_db_connector(object):

    def __init__(self):
        self.mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="password",
          database="fplanalysis"
        )
        self.mycursor = self.mydb.cursor()


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

    def get_top_scorer(self):
        sql = "SELECT first_name, last_name, current_points FROM players ORDER BY current_points LIMIT 1"
        self.mycursor.execute(sql)
        myresult = self.mycursor.fetchall()
        for x in myresult:
            print(x)

if __name__ == "__main__":
    db = sql_db_connector()
    player = player_object.player_obj(1, "first", "last", 0, 0, 1, 0, 1, 1)
    db.clear_all()
    db.use_db()
    db.insert_player(player)
    db.get_top_scorer()
