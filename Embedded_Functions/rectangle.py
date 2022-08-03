# Have a list of pairs of numbers denoting the sides of a rectangle.
# 
#           [(3,4),(10,3),(5.6),(1,9)]
# 
# Now write a function that calculates the area of the rectangle according to the side lengths and apply this function to each element of this list to print a list like this.
# 
#           [12, 30, 30, 9]
# 
# Note : Try to use the map() function.

from functools import reduce


def calculate(tuple):
    def area(x, y):
        return x*y
    return reduce(area, tuple)

lines = [(3,4),(10,4),(5,6),(1,9)]
areas = list(map(calculate, lines))
print(areas)