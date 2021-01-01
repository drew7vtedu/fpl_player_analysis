# why I feel the need to test these I'm not exactly sure
from data_analysis import fantasy_value_metrics as fvm
import unittest


class TestFantasyAnalysisDriver(unittest.TestCase):


    def setUp(self):
        # method intentionally left blank for now
        pass

    def test_points_scored_per_90(self):
        self.assertEqual(fvm.points_scored_per_90(0,0), 0)
        # tests that we dont accidentaly divide by 0
        self.assertEqual(fvm.points_scored_per_90(100, 0), 0)
        self.assertEqual(fvm.points_scored_per_90(100, 90), 100)


    def test_points_scored_per_match(self):
        self.assertEqual(fvm.points_scored_per_match(0,0), 0)
        self.assertEqual(fvm.points_scored_per_match(100, 0), 0)
        self.assertEqual(fvm.points_scored_per_match(100, 1), 100)

    def test_points_scored_per_match_per_mil(self):
        self.assertEqual(fvm.points_scored_per_match_per_mil(0, 0, 0), 0)
        self.assertEqual(fvm.points_scored_per_match_per_mil(1, 0, 0), 0)
        self.assertEqual(fvm.points_scored_per_match_per_mil(0, 1, 0), 0)
        self.assertEqual(fvm.points_scored_per_match_per_mil(1, 1, 1), 1)
        # here we'll get a decimal, python dynamic typing means its not truncated
        self.assertEqual(fvm.points_scored_per_match_per_mil(1, 1, 2), 0.5)


    def test_value_added_per_mil(self):
        self.assertEqual(fvm.value_added_per_mil(0, 0, 0), 0)
        self.assertEqual(fvm.value_added_per_mil(0, 1, 0), 0)
        self.assertEqual(fvm.value_added_per_mil(1, 0, 0), 0)
        self.assertEqual(fvm.value_added_per_mil(100, 10, 1), 8)
        self.assertEqual(fvm.value_added_per_mil(100, 0, 1), 0)
        self.assertEqual(fvm.value_added_per_mil(100, 1, 2), 49)


    def tearDown(self):
        # method intentionally left blank for now
        pass

if __name__ == "__main__":
    unittest.main()
