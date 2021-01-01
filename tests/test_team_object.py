import unittest
from data_analysis import team_object as to

class TestTeamObject(unittest.TestCase):


    def setUp(self):
        # constructor takes arguments (id, goals_for, goals_against, xg, xga)
        self.team1 = to.team(0, 10, 5, 10.33, 7.62)

    def test_constructor(self):
        self.assertEqual(self.team1.id, 0)
        self.assertEqual(self.team1.goals_for, 10)
        self.assertEqual(self.team1.goals_against, 5)
        self.assertEqual(self.team1.xg, 10.33)
        self.assertEqual(self.team1.xga, 7.62)

    def test_set_goals_for(self):
        self.assertEqual(self.team1.goals_for, 10)
        self.team1.set_goals_for(12)
        self.assertEqual(self.team1.goals_for, 12)

    def test_set_goals_against(self):
        self.assertEqual(self.team1.goals_against, 5)
        self.team1.set_goals_against(6)
        self.assertEqual(self.team1.goals_against, 6)

    def test_set_xg(self):
        self.assertEqual(self.team1.xg, 10.33)
        self.team1.set_xg(10.99)
        self.assertEqual(self.team1.xg, 10.99)

    def test_set_xga(self):
        self.assertEqual(self.team1.xga, 7.62)
        self.team1.set_xga(8.1)
        self.assertEqual(self.team1.xga, 8.1)


if __name__ == "__main__":
    unittest.main()
