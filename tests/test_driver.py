# some relative imports from the parent directory
from data_analysis import player_object as player
from data_analysis import fantasy_value_metrics as metrics
from data_analysis import fpl_analysis_driver as fad
import pytest
import csv

# function to test createAccount
# create current functionality: create new account, reject existing user, other unkown error
# login current functionality: account doesn't exist, password matches, password doesn't match
class TestFantasyAnalysisDriver(unittest.TestCase):

    def __init__(self):
        self.ly_test = "../data/test_ly_data.csv"
        self.cy_test = "../data/test_cy_data.json"
        self.test_db = "../data/test_db.csv"

    def setUp(self):
        ly_test = "../data/test_ly_data.csv"
        cy_test = "../data/test_cy_data.json"
        test_db = "../data/test_db.csv"


    def test_create_player_db(self):
        fad.create_player_db(self.ly_test, self.cy_test, self.test_db)
        self.assertTrue(os.path.isfile(test_db))


    def tearDown(self):
        # method intentionally left blank for now
        pass


if __name__ == "__main__":
    unittest.main()
