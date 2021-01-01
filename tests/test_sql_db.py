import unittest
from data_analysis import sql_db

class TestSqlDb(unittest.TestCase):

    def setUp(self):
        self.db = sql_db.sql_db_connector()
