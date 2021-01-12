import unittest
from data_analysis import sql_db
from data_analysis import player_object as po
from data_analysis import team_object as to
from data_analytice import fixture object as fo


class TestSqlDb(unittest.TestCase):

    def setUp(self):
        self.db = sql_db.sql_db_connector()
        self.db.use_test_db()


    def test_create_db(self):
        self.db.create_test_db()


    def test_insert_player(self):
        player = player_object.player_obj(1, "first", "last", 0, 0, 1, 0, 1, 1)
        self.db.insert_player(player)
        self.assertEqual(db.get_player_by_name("first", "last").get_id(), 1)

    def test_remove_player(self):
        self.db.remove_player_by_id(1)


if __name__ == "__main__":
    unittest.main()
