#!env/bin/python
import os
import unittest
from app import create_app

class UtilsTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app().test_client()

    def tearDown(self):
        pass

    def test_home(self):
        response = self.app.get("/", follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_home_data(self):
        response = self.app.get("/", follow_redirects=True)
        self.assertRegex(response.data.decode(), "(95.stores)")


if __name__ == "__main__":
    unittest.main()
