"""
Problem 2

Try to find out if a number you received from the user is the "Armstrong" number.
For example, if a number is 4 digits and the sum of each of its digits to the power 4
If (3rd power for 3-digit numbers) is equal to that number, this number is called "Armstrong" number.

For example: 1634 = 1^4 + 6^4 + 3^4 + 4^4
"""

while True:
    number = int(input("Enter A Number: "))
    digit_number = len(str(number))
    digits = number
    total = 0

    while digits > 0:
        digit = digits % 10
        digits = (digits - digit) / 10
        total += digit ** digit_number

    if total == number:
        print(f"Number {number} Is A Armstrong Number...")
        break
    else:
        print(f"Number {number} Is Not A Armstrong Number...")
        break
