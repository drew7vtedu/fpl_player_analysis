import unittest
from dotenv import load_dotenv
load_dotenv()
from data_analysis import sql_db


class TestSqlDb(unittest.TestCase):

    def setUp(self):
        self.db = sql_db.sql_db_connector()
        db.use_test_db()


    def test_create_db(self):
        db.create_test_db()
