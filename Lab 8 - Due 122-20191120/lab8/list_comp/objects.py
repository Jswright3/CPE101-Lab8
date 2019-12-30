# Lab 8
# Name: John Wright
# Instructor: S. Einakian
# Section: 101-05


class Point:
   def __init__(self,x,y):
      self.x = x
      self.y = y

   def __repr__(self):
      return 'Point(x:{}, y:{} )'.format(self.x, self.y)

   def __eq__(self, other):
      if self.x == other.x and self.y == other.y:
         return True
      else:
         return False


class Circle:
   def __init__(self,point,r):
      self.point = point
      self.r = r
   def __repr__(self):
      return 'Circle({}, r:{} )'.format(self.point,self.r)

