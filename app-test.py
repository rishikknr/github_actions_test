import unittest
from app import add, multiply


class TestApp(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 20), 30)

    def test_multiply(self):
        self.assertEqual(multiply(5, 4), 20)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)


if __name__ == "__main__":
    unittest.main()
