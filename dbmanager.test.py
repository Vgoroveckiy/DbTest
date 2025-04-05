import unittest

from dbmanager import DatabaseManager


class TestDatabaseManager(unittest.TestCase):
    def setUp(self):
        self.db = DatabaseManager(":memory:")
        self.db.create_tables()

    def tearDown(self):
        self.db.close()


def test_get_user_data(self):
    # Add a test user to the database
    test_name = "John Doe"
    test_email = "john@example.com"
    user_id = self.db.add_user(test_name, test_email)

    # Call the method being tested
    result = self.db.get_user_data(user_id)

    # Assert that the returned data matches the test user's data
    self.assertIsNotNone(result)
    self.assertEqual(result[0], test_name)
    self.assertEqual(result[1], test_email)


def test_get_user_data_non_existent_user(self):
    # Attempt to get data for a non-existent user
    non_existent_user_id = 9999
    result = self.db.get_user_data(non_existent_user_id)

    # Assert that the result is None
    self.assertIsNone(result)


def test_get_user_data_special_characters(self):
    # Add a test user with special characters in the name
    test_name = "John O'Connor-Müller"
    test_email = "john.special@example.com"
    user_id = self.db.add_user(test_name, test_email)

    # Call the method being tested
    result = self.db.get_user_data(user_id)

    # Assert that the returned data matches the test user's data
    self.assertIsNotNone(result)
    self.assertEqual(result[0], test_name)
    self.assertEqual(result[1], test_email)


def test_get_user_data_large_user_id(self):
    # Add a test user with a very large ID
    large_user_id = 9223372036854775807  # Maximum value for SQLite INTEGER
    test_name = "Large ID User"
    test_email = "large.id@example.com"
    self.db.cursor.execute(
        "INSERT INTO users (id, name, email) VALUES (?, ?, ?)",
        (large_user_id, test_name, test_email),
    )
    self.db.conn.commit()

    # Call the method being tested
    result = self.db.get_user_data(large_user_id)

    # Assert that the returned data matches the test user's data
    self.assertIsNotNone(result)
    self.assertEqual(result[0], test_name)
    self.assertEqual(result[1], test_email)


def test_get_user_data_identical_names(self):
    # Add two users with identical names but different emails
    test_name = "John Smith"
    test_email1 = "john1@example.com"
    test_email2 = "john2@example.com"
    user_id1 = self.db.add_user(test_name, test_email1)
    user_id2 = self.db.add_user(test_name, test_email2)

    # Call the method being tested for both users
    result1 = self.db.get_user_data(user_id1)
    result2 = self.db.get_user_data(user_id2)

    # Assert that the returned data matches each user's data
    self.assertIsNotNone(result1)
    self.assertEqual(result1[0], test_name)
    self.assertEqual(result1[1], test_email1)

    self.assertIsNotNone(result2)
    self.assertEqual(result2[0], test_name)
    self.assertEqual(result2[1], test_email2)

    # Assert that the emails are different despite identical names
    self.assertNotEqual(result1[1], result2[1])


def test_get_user_data_unicode_characters(self):
    # Add a test user with unicode characters in name and email
    test_name = "Jörg Müller"
    test_email = "jörg.müller@exämple.com"
    user_id = self.db.add_user(test_name, test_email)

    # Call the method being tested
    result = self.db.get_user_data(user_id)

    # Assert that the returned data matches the test user's data
    self.assertIsNotNone(result)
    self.assertEqual(result[0], test_name)
    self.assertEqual(result[1], test_email)


def test_get_user_data_negative_user_id(self):
    # Attempt to get data for a user with a negative ID
    negative_user_id = -1
    result = self.db.get_user_data(negative_user_id)

    # Assert that the result is None
    self.assertIsNone(result)


def test_get_user_data_float_user_id(self):
    # Add a test user with an integer ID
    test_name = "Float User"
    test_email = "float@example.com"
    user_id = self.db.add_user(test_name, test_email)

    # Call the method being tested with a floating point ID
    float_user_id = float(user_id) + 0.7
    result = self.db.get_user_data(float_user_id)

    # Assert that the returned data matches the test user's data
    self.assertIsNotNone(result)
    self.assertEqual(result[0], test_name)
    self.assertEqual(result[1], test_email)


def test_get_user_data_concurrent_queries(self):
    # Add multiple test users to the database
    test_users = [
        ("Alice", "alice@example.com"),
        ("Bob", "bob@example.com"),
        ("Charlie", "charlie@example.com"),
    ]
    user_ids = [self.db.add_user(name, email) for name, email in test_users]

    # Simulate concurrent queries
    import threading

    def query_user(user_id):
        result = self.db.get_user_data(user_id)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], test_users[user_ids.index(user_id)][0])
        self.assertEqual(result[1], test_users[user_ids.index(user_id)][1])

    threads = [threading.Thread(target=query_user, args=(uid,)) for uid in user_ids]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    # Verify that all users' data is still correct after concurrent queries
    for user_id, (name, email) in zip(user_ids, test_users):
        result = self.db.get_user_data(user_id)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], name)
        self.assertEqual(result[1], email)


if __name__ == "__main__":
    unittest.main()
