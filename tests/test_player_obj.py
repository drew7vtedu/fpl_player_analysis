# yay writing tests for getters and setters
import unittest
from data_analysis import player_object as po

class TestPlayerObject(unittest.TestCase):

    def setUp(self):
        # constructor takes arguments (id, first_name, last_name, pls, cp, price, ly_mins, mins, team)
        self.player1 = po.player_obj(1, "first", "last", 100, 10, 1.0, 360, 90, 0)


    def test_constructor(self):
        self.assertEqual(self.player1.id, 1)
        self.assertEqual(self.player1.first_name, "first")
        self.assertEqual(self.player1.last_name, "last")
        self.assertEqual(self.player1.points_last_season, 100)
        self.assertEqual(self.player1.current_points, 10)
        self.assertEqual(self.player1.price, 1)
        self.assertEqual(self.player1.ly_minutes, 360)
        self.assertEqual(self.player1.minutes, 90)
        self.assertEqual(self.player1.team_id, 0)

    def test_set_pls(self):
        self.assertEqual(self.player1.points_last_season, 100)
        self.player1.set_pls(90)
        self.assertEqual(self.player1.points_last_season, 90)

    def test_set_ly_minutes(self):
        self.assertEqual(self.player1.ly_minutes, 360)
        self.player1.set_ly_minutes(90)
        self.assertEqual(self.player1.ly_minutes, 90)

    def test_set_points(self):
        self.assertEqual(self.player1.current_points, 10)
        self.player1.set_points(20)
        self.assertEqual(self.player1.current_points, 20)

    def test_set_minutes(self):
        self.assertEqual(self.player1.minutes, 90)
        self.player1.set_minutes(180)
        self.assertEqual(self.player1.minutes, 180)

    def test_set_price(self):
        self.assertEqual(self.player1.get_price(), 1)
        self.player1.set_price(2.0)
        self.assertEqual(self.player1.get_price(), 2)

    def test_set_team(self):
        self.assertEqual(self.player1.team_id, 0)
        self.player1.set_team(1)
        self.assertEqual(self.player1.team_id, 1)

    def test_set_xg(self):
        self.assertEqual(self.player1.xg, 0)
        self.player1.set_xg(2.5)
        self.assertEqual(self.player1.xg, 2.5)

    def test_set_xa(self):
        self.assertEqual(self.player1.xa, 0)
        self.player1.set_xa(1.8)
        self.assertEqual(self.player1.xa, 1.8)

    def test_to_dict(self):
        dict = self.player1.to_dict()
        self.assertEqual(dict["first_name"], "first")
        self.assertEqual(dict["last_name"], "last")
        self.assertEqual(dict["points_last_season"], 100)
        self.assertEqual(dict["current_points"], 10)
        self.assertEqual(dict["price"], 1.0)
        self.assertEqual(dict["ly_minutes"], 360)
        self.assertEqual(dict["minutes"], 90)
        self.assertEqual(dict["xg"], 0)
        self.assertEqual(dict["xa"], 0)
        self.assertEqual(dict["team"], 0)

if __name__ == "__main__":
    unittest.main()
