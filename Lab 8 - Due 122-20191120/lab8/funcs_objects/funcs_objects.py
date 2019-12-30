# Lab 8
# Name: John Wright
# Instructor: S. Einakian
# Section: 101-05
from objects import *
from math import sqrt


def distance(P1, P2):
   # 2 object -> float
   return sqrt(((P1.x-P2.x)**2)+((P1.y-P2.y)**2))

def circles_overlap(C1, C2):
   # 2 object -> bool
   if distance(C1.point,C2.point) < (C1.r + C2.r):
      return True
   else:
      return False
