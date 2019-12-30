import unittest
from objects import *

class TestCases(unittest.TestCase):
   def test_equality(self):
      P1 = Point(3, 5)
      P2 = Point(2, 1)
      P3 = Point(3, 4)
      P4 = Point(3, 4)
      self.assertFalse(P1 == P2)
      self.assertTrue(P3 == P4)


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

