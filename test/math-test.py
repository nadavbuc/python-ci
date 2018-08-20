import unittest
from src.math import Math


class Mathtest(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(Math.addition(3,4), 8)
