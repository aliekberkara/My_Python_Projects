"""
1- Find the numeric values in the list elements.

2- Make sure every entry you receive is a number unless the user enters the 'q' value. 
Otherwise, write an error message.

3- Create the factorial function and give error messages for the value that comes to the function.
"""

# Problem - 1

list = ["1", "6", "10a", "20a0", "abc", "20", "100"]

for i in list:
    try:
        result = int(i)
        print(result)
    except ValueError:
        continue

# Problem - 2

while True:
    number = input("Number: ")
    if number == 'q':
        print("Exiting...")
        break
    else:
        try:
            result = float(number)
            print(result)
        except ValueError:
            print('Invalid Number!')
            continue

# Problem - 3

def factorial(x):
    x = int(x)

    if x < 0:
        raise ValueError('Negative Value')
    
    result = 1

    for i in range(1, x+1):
        result *= i
    
    return result

for x in [1,6,5,10,"10a", -3]:
    try:
        y = factorial(x)
    except ValueError as err:
        print(err)
        continue
    print(y)
