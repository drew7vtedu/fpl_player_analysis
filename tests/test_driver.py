# when run from the command line you must be in the same directory
#   because of the relative path used for file names
# added parent folder to $PYTHONPATH to allow these module imports
from data_analysis import player_object as player
from data_analysis import fantasy_value_metrics as metrics
from data_analysis import fpl_analysis_driver as fad
import unittest
import csv
import os

class TestFantasyAnalysisDriver(unittest.TestCase):

    # def __init__(self):
    #     self.ly_test = "../data/test_ly_data.csv"
    #     self.cy_test = "../data/test_cy_data.json"
    #     self.test_db = "../data/test_db.csv"

    def setUp(self):
        # relative path to file names
        self.ly_test = "./test_data/test_ly_data.csv"
        self.cy_test = "./test_data/test_cy_data.json"
        self.test_db = "./test_data/test_db.csv"


    def test_create_player_db(self):
        fad.create_player_db(self.ly_test, self.cy_test, self.test_db)
        self.assertTrue(os.path.isfile(self.test_db))


    def tearDown(self):
        # method intentionally left blank for now
        pass


if __name__ == "__main__":
    unittest.main()
