import unittest
import MySQLdb

class TestStateCreation(unittest.TestCase):
    def setUp(self):
        # Set up a connection to your isolated database
        self.db = MySQLdb.connect(host='localhost', user='root', passwd='Gkipl@g@t1', db='unittest')
        self.cursor = self.db.cursor()

    def tearDown(self):
        # Clean up resources after the test
        self.cursor.close()
        self.db.close()

    def test_add_state_record(self):
        # Get the initial count of records in the 'states' table
        self.cursor.execute("SELECT COUNT(*) FROM states")
        initial_count = self.cursor.fetchone()[0]

        # Execute the console command (e.g., create a new state record)
        # Replace this with your actual command
        # For example:
        self.cursor.execute("INSERT INTO states (name) VALUES ('California')")
        self.db.commit()

        # Get the count of records after executing the command
        self.cursor.execute("SELECT COUNT(*) FROM states")
        final_count = self.cursor.fetchone()[0]

        # Check if the difference is +1
        self.assertEqual(final_count, initial_count + 1, "Adding a state record failed")

if __name__ == '__main__':
    unittest.main()
