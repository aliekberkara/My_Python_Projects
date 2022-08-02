"""
Write a program that converts an entered number into binary.
"""

def convert(number, binaryText = ""):
    if number == 0:
        return binaryText
    binary = number % 2
    binaryText = str(binary) + binaryText
    return convert(number//2, binaryText)
binaryText = ""
number = int(input('Enter a number: '))

print(convert(number, binaryText))
