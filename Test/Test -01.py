# test_myapp.py
import unittest
from main import dodavannya, a, b

class TestMyApp(unittest.TestCase):
    def test_dodavannya(self):
        result = dodavannya(a, b)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()