import unittest
import sqlite3
from addition import app

class IntegrationTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        # Set up the database connection
        self.connection = sqlite3.connect(':memory:')  # Use an in-memory database for tests
        self.cursor = self.connection.cursor()
        # Set up necessary tables and data for testing
        self.cursor.execute('''CREATE TABLE example (id INTEGER PRIMARY KEY, value TEXT)''')
        self.connection.commit()

    def tearDown(self):
        self.connection.close()

    def test_database_integration(self):
        # Test inserting a record
        self.cursor.execute("INSERT INTO example (value) VALUES ('test')")
        self.connection.commit()

        self.cursor.execute("SELECT * FROM example WHERE value='test'")
        row = self.cursor.fetchone()
        self.assertIsNotNone(row)

if __name__ == '__main__':
    unittest.main()
