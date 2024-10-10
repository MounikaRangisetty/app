import unittest
from addition import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add(self):
        response = self.app.get('/add?x=1&y=2')
        json_data = response.get_json()
        self.assertEqual(json_data['result'], 3)
        self.assertEqual(response.status_code, 200)

    def test_add_missing_params(self):
        response = self.app.get('/add?x=1')
        json_data = response.get_json()
        self.assertEqual(json_data['error'], "Missing parameters x or y")
        self.assertEqual(response.status_code, 400)

    def test_health_check(self):
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
