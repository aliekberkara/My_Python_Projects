# Have a list like this.
# 
#      [1,2,3,4,5,6,7,8,9,10]
# 
# Write a function that prints the sum of the even numbers in this list.
# 
# Note: First extract the even numbers with the filter() function. Then use the reduce() function.

from functools import reduce


list1 = [1,2,3,4,5,6,7,8,9,10]

even = list(filter(lambda x: x%2==0, list1))

def add(x, y):
    return x+y

print(reduce(add, even))
