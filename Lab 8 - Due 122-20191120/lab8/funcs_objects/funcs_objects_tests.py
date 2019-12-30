import unittest
from objects import *
from funcs_objects import *

class TestCases(unittest.TestCase):
   def test_point(self):
      P1 = Point(3,5)
      P2 = Point(9,1)
      self.assertEqual(P1.x,3)
      self.assertEqual(P2.y,1)

   def test_circle(self):
      P1 = Point(3, 5)
      P2 = Point(9, 1)
      C1 = Circle(P1,4)
      C2 = Circle(P2,1)
      self.assertEqual(C1.point.x,3)
      self.assertEqual(C2.r,1)

   def test_distance(self):
      P1 = Point(3, 5)
      P2 = Point(9, 1)
      P3 = Point(1, 8)
      P4 = Point(3, 3)
      self.assertEqual(distance(P1,P2),7.211102550927978)
      self.assertEqual(distance(P3,P4),5.385164807134504)

   def test_circles_overlap(self):
      P1 = Point(3, 5)
      P2 = Point(9, 1)
      P3 = Point(4, 4)
      P4 = Point(5, 5)
      C1 = Circle(P1, 1)
      C2 = Circle(P2, 1)
      C3 = Circle(P3, 5)
      C4 = Circle(P4, 5)
      self.assertFalse(circles_overlap(C1,C2))
      self.assertTrue(circles_overlap(C3,C4))

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

