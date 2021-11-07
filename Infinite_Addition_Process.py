"""
Problem 4 
In each "while" loop, get a number from the user and enter the numbers entered by the user into a "total" and
add it to the variable. When the user presses the "q" key, terminate the loop and print the "total" variable to the screen.
"""

total = 0
while True:
    number = input("Enter A Number:")
    if number == 'q':
        print(f"Total:{total}")
        break
    else:
        number = int(number)
        total += number
