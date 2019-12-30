# Lab 8
# Name: John Wright
# Instructor: S. Einakian
# Section: 101-05
from objects import *


def distance_all(list):
   origin = Point(0,0)
   new_list = [distance(i,origin) for i in list]
   return new_list

def are_in_first_quadrant(list):
   first_quad = [i for i in list if i.x > 0 and i.y > 0]
   if len(list) == len(first_quad):
      return True
   else:
      return False






