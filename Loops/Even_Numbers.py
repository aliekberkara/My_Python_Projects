"""
Problem 6

Try to put only even numbers from 1 to 100 into a list using "list comprehension".
"""

even = [number for number in range(1, 101) if number % 2 == 0]
print(even)
