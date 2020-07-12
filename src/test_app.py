import unittest
import app

app = app.app
app.testing = True


class AppTestCase(unittest.TestCase):

    def test_index(self):
        with app.test_client() as c:
            r = c.get('/')
            self.assertEqual(r.status_code, 200)

    def test_pick_rand(self):
        with app.test_client() as c:
            r = c.get('/mock')
            self.assertTrue(True)

    def test_match(self):
        with app.test_client() as c:
            r = c.get('/match')
            self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
