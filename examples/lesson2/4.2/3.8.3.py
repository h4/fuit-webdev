# -*- encoding: utf-8 -*-
"""
Вывод класса
"""

class Point:
   def __init__( self, xValue = 0, yValue = 0 ):
      self.x = xValue
      self.y = yValue

   def __str__( self ):
      return "( %d, %d )" % ( self.x, self.y )      

point = Point( 72, 115 )

print "X coordinate is:", point.x
print "Y coordinate is:", point.y

point.x = 10
point.y = 10

print "The new location of point is:", point   